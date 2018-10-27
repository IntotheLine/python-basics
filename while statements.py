# while statements are lopped as long the conditions are true

spam = 0
while spam < 5:
    print("Hello World")
    spam = spam + 1

# yourname loop

name = " "
while name != "your name":
    print("please enter your name")
    name = input()
print("thanks to you")

#endless loop, because True stays True
while True:
    print("Hello World")

#while can be combined if If/else/elif

name = " "
while True:
    print("please enter your name")
    name = input()
    if name == "your name":
        break #jumps immediatly out of the whileloop
print("thank you")

#continue statments, turns the loop back to the beginning to recheck conditions

spam = 0
while spam <= 5:
    spam = spam +1
    if spam == 3:
        continue
    print("spam is" + str(spam))

    spam = 0
while spam <= 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is" + str(spam))
    if spam == 4: #if 4, functions jumps to break, and exits loop, break is aslong ignored as spam == 4
        break

#pythontutor.com helps a lot here :-) 
