# Spiel des Lebens.py

import math
import pyperclip
import random

# needs to defined
# playernames
# playercolours
# amount of playrounds
# houses
# cars
# neutral fields
# house fields
# car fields
# random step generator
# add Salery each step
# define selery by promotion
# the idea is with an random generator to add an dictionary

# Starts the game asks for the players, theire colours and some easy checks.
print('welcome to Game of Live')
print('this is a ongoing development project')
print('please enter the number of players, able up to 4')


players = input()
while not players.isdecimal():
    print('please enter a number between 2 and 4')
    players = input()

if players.isdecimal():
    print('Welcome you ' + players + ' players')

if players <= '1':
    print('this is for at least two players yet')
    print('you have to enter again between 2 and 4 ;-)')
    players = input()

if players == '2':
    print('please enter your name for player 1')
    PlayerOneName = input()
    print('please enter your name for player 2')
    PlayerTwoName = input()
    True

print('Welcome %s and %s to your game' % (PlayerOneName, PlayerTwoName))

PlayerColourSelection = {'1': 'yellow', '2': 'red', '3': 'green', '4': 'blue'}
print('Please choose your colour' + PlayerOneName)

print('1 for yellow, 2 for red, 3 for green, 4 for blue')
PlayerOneColourInput = input()
if PlayerOneColourInput.isdecimal():
    PlayerOneColour = PlayerColourSelection.get(PlayerOneColourInput)
    if not PlayerOneColourInput.isdecimal():
        print('1 for yellow, 2 for red, 3 for green, 4 for blue')
        PlayerOneColourInput = input()
        print(PlayerOneColour)

print('Please choose your colour ' + PlayerTwoName)
PlayerTwoColourInput = input()
while PlayerTwoColourInput == PlayerOneColourInput:
    print(PlayerTwoName + ' I am sorry, but you can not choose the same colour as Player One')
    PlayerTwoColourInput = input()

if PlayerTwoColourInput.isdecimal():
    PlayerTwoColour = PlayerColourSelection.get(PlayerTwoColourInput)
    print(PlayerTwoColour)

print('%s has the colour %s, %s has the colour %s' % (PlayerOneName, PlayerOneColour, PlayerTwoName, PlayerTwoColour))

# this section ads the yearly income of the players
PlayerOneIncome = int(5000)
PlayerTwoIncome = int(5000)

PlayerOneWallet = int(0)
PlayerTwoWallet = int(0)


def Salery(PlayerOneIncome, PlayerTwoIncome):
    PlayerOneIncome = PlayerOneWallet + PlayerOneIncome
    PlayerTwoIncome = PlayerTwoWallet + PlayerTwoIncome
