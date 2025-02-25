import os
from pickle import NONE

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method =="Post":
        if not request.form.get("money").isdigit():
            return apology("You cannot purchase partial shares.")
        else:
            money = int(request.form.get("money"))
            db.execute("UPDATE users SET cash = cash + ? where id = ?", money, (session["user_id"]))
            return redirect("/")
    else:
       return render_template("add.html")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    grandtotal = 0
    portfolios = db.execute(
        "SELECT symbol,user,SUM(numshare) as totalshares FROM shares WHERE user = ? ORDER BY symbol", (session["user_id"]))
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    money = round(user_cash[0]["cash"], 2)
    print(portfolios)
    if portfolios[0]["user"] == None:
        total = money
        grandtotal += total
        return render_template("nostock.html", money=usd(money), total=usd(total), grandtotal=usd(grandtotal))
    else:
        for portfolio in portfolios:
            stock = lookup(portfolio["symbol"])
            name = stock["name"]
            price = stock["price"]
            symbol = stock["symbol"]
            share = portfolio["totalshares"]
            total = price * share
            grandtotal += total + money
    return render_template("index.html", name=name, price=usd(price), symbol=symbol, share=share, money=usd(money), total=usd(total), grandtotal=usd(grandtotal))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        if not request.form.get("shares").isdigit():
            return apology("You cannot purchase partial shares.")
        else:
            share = int(request.form.get("shares"))
        quote = lookup(symbol)
        if quote == None:
            return apology("Stock Does not Exist")
        else:
            name = quote["name"]
            price = quote["price"]
            symbol = quote["symbol"]
            totalstonks = price * share
            user = session["user_id"]
            cash = db.execute("SELECT cash from users where id = (?)", user)
            money = cash[0]["cash"]

            if totalstonks < money:
                money = money - totalstonks
                db.execute("UPDATE users SET cash = ? where id = ?", money, user)
                total = totalstonks + money
                price = usd(price)
                totalstonks = usd(totalstonks)
                money = usd(money)
                db.execute("INSERT INTO shares (user,compname, shareprice,symbol,TotalStonks,numshare) VALUES (?,?,?,?,?,?)",
                           user, name, price, symbol, totalstonks, share)
                return render_template("bought.html", name=name, price=price, symbol=symbol, share=share, totalstonks=totalstonks, money=money, total=total)
            else:
                return apology("Sorry you cannot afford this stock")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    grandtotal = 0
    portfolios = db.execute(
        "SELECT symbol,user,SUM(numshare) as totalshares FROM shares WHERE user = ? ORDER BY symbol", (session["user_id"]))
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    money = round(user_cash[0]["cash"], 2)
    print(portfolios)
    if portfolios[0]["user"] == None:
        total = money
        grandtotal += total
        return render_template("nostock.html", money=usd(money), total=usd(total), grandtotal=usd(grandtotal))
    else:
        for portfolio in portfolios:
            stock = lookup(portfolio["symbol"])
            name = stock["name"]
            price = stock["price"]
            symbol = stock["symbol"]
            share = portfolio["totalshares"]
            total = price * share
            grandtotal += total + money
    return render_template("index.html", name=name, price=usd(price), symbol=symbol, share=share, money=usd(money), total=usd(total), grandtotal=usd(grandtotal))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if quote == None:
            return apology("Stock Does not Exist")
        else:
            name = quote["name"]
            price = usd(quote["price"])
            symbol = quote["symbol"]
            return render_template("quoted.html", name=name, price=price, symbol=symbol)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        password_check = request.form.get("confirmation")
        rows = db.execute("SELECT id FROM users WHERE username = ?", name)

        if len(rows) >= 1:
            return apology("Username is Already Taken")

        if name == '' or password == '' or password_check == '':
            return apology("Please fill in blanks")
        if password == password_check:
            genhash = generate_password_hash(password)
        else:
            return apology("Passwords do not Match or Is Blank")

        db.execute("INSERT INTO users (username, hash) VALUES (?,?)", name, genhash)
        return render_template("login.html")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not request.form.get("shares").isdigit():
            return apology("You cannot purchase partial shares.")
        else:
            share = int(request.form.get("shares"))
        quote = lookup(symbol)
        if quote == None:
            return apology("Stock Does not Exist")
        else:
            name = quote["name"]
            price = quote["price"]
            symbol = quote["symbol"]
            totalstonks = price * share
            user = session["user_id"]
            cash = db.execute("SELECT cash from users where id = (?)", user)
            money = cash[0]["cash"]
            money = float(money) - totalstonks
            db.execute("UPDATE users SET cash = ? where id = ?", money, user)
            total = totalstonks + money
            price = usd(price)
            totalstonks = usd(totalstonks)
            money = usd(money)
            db.execute("INSERT INTO shares (user,compname, shareprice,symbol,TotalStonks,numshare) VALUES (?,?,?,?,?,?)",
                       user, name, price, symbol, totalstonks, share)
            return render_template("bought.html", name=name, price=price, symbol=symbol, share=share, totalstonks=totalstonks, money=money, total=total)
    else:
        return render_template("sell.html")
