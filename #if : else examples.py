# if / else examples

name = "alice"
if name == "alice":
    print("hi alice")
print("done")

# password check
password = "swordfish"
in_password = input()
if password == in_password:
    print("access granted")
else:
    print("stay out dude")

# elif = else / if
# elif statements have to be in an correct order, because the first true condition will be taken, rest of elif's will be skipped
# else can be combined and will be executed if all elif's are wrong

print("enter a name")
name = input()
if name:
    print("Thanks for entering your name")
elif name == "jonas":
    print("Hi Boss")
else:
    print("You did not enter a name.")
