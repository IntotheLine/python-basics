spam = 0
while spam <= 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is" + str(spam))
    if spam == 4: #if 4, functions jumps to break, and exits loop, break is aslong ignored as spam == 4
        break

#pythontutor.com helps a lot here :-) 