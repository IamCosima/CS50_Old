from cs50 import get_int

# Prompting the user to enter a width value until it is between 1 and 8 inclusive
while True:
    Width = get_int("Height: ")
    if Width > 0 and Width <= 8:
        break
# print pyramid
# loop for row of Pyramid
for i in range(Width):
    # loop for spaces making right allighed of Pyramid
    for j in range(Width - i - 1, 0, - 1):
        print(" ", end="")
    # loop for Hashes making Pyramid
    for b in range(i+1):
        print("#", end="")
    print("\n", end="")
