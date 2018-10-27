# input validation.py

# Input Validation
print("How many cats do you have")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That are many cats")
    else:
        print("You have a poor number of cats")
except ValueError:
    print("You did not enter a number")
