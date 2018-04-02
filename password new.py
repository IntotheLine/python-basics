# passsword new.py
print("Hello World")
print("please enter password")
password = "world"
user_password = input()
while password != user_password:
    print("please enter password")
    user_password = input()
    if password == user_password:
        break
print("welcome")

#password loop until you enter the correct one, next attempt with an counter of 3
