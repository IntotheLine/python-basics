# This is a number guess game.py

import random
print("Hey, whats your name")
name = input()

print("Choose your difficulty by entering 1 = easy, 2 = normal, 3 = hard")
game = int(input())
if game > 3:
    print("error, please enter a number between 1 and 3")
    game = int(input())
elif game < 0:
    print("error, please enter a number between 1 and 3")
    game = int(input())
elif game == 1:
    secretNumber = random.randint(1, 20)
    print("take your guesses now")

for guessTaken in range(1, 7):
    guess = int(input())
    if guess < secretNumber:
        print("lowbob")
    elif guess > secretNumber:
        print("highbob")
    else:
        break  # this condition is correct

elif game == 2:
    secretNumber = random.randint(1, 100)
    print("Take your guesses now")

for guessTaken in range(1, 7):
    guess = int(input())
    if guess < secretNumber:
        print("lowbob")
    elif guess > secretNumber:
        print("highbob")
    else:
        break  # this condition is correct

    elif game == 3:
    secretNumber = random.randint(1, 1000)
    print("Take your guesses now")
for guessTaken in range(1, 7):
    guess = int(input())
    if guess < secretNumber:
        print("lowbob")
    elif guess > secretNumber:
        print("highbob")
    else:
        break  # this condition is correct

if guess == secretNumber:
    print("GJ")
else:
    print("correct is" + str(secretnumber))
