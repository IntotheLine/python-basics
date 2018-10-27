# Number Guess Game advanced.py

import random
print("Whats your name")
name = input()

print(name + "how many trys you'd like to have")  # ask for the name
trys = int(input())  # sets the range of trys in the 4 loop
print(name + "please enter a number")
rangenumber = int(input())
secretnumber = random.randint(1, rangenumber + 1)  # needs a plus
print(secretnumber)
# this is the loop for the guesses, the secretnumber is between 0 and players choice
for guessTaken in range(0, trys):
    guess = int(input())
    if guess > secretnumber:
        print("too high")
    elif guess < secretnumber:
        print("too low")
    elif guess == secretnumber:
        break
    else:
        print("give it another try")

print("Good Job")
