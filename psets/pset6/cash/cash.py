from cs50 import get_float

Counter = 0
# Prompting the user to enter a width value until it is greater than 1
while True:
    Owed = get_float("Enter Owed Amount: ")
    if Owed > 0:
        break
# Changing from dollars to cents
# Rounding off to stop floating point precision errors
Cents = round(Owed * 100)

# Checking if 25 can be subtracted
while Cents >= 25:
    Cents = Cents - 25
    Counter += 1

# Checking if 10 can be subtracted
while Cents >= 10:
    Cents = Cents - 10
    Counter += 1
# Checking if 5 can be subtracted
while Cents >= 5:
    Cents = Cents - 5
    Counter += 1

    # Checking if 1 can be subtracted
while Cents >= 1:
    Cents = Cents - 1
    Counter += 1
    # Returning Value to the user
print(Counter)