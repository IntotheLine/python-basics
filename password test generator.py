# random password generator
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"

generator = {1: a, 2: b, 3: c, 4: d, 5: e}
difficulty = {1: str(5), 2: str(10), 3: str(20)}

print("please choose your passwor lenght: 1 = 5, 2 = 10, or 3 = 20chars long")
password.len(0, )

lengthInput = int(input())
length = difficulty.get(lengthInput)

print(str(length))
for password in range(0, lengthInput - 1):
    x1 = generator.get(int(difficulty))
    password = generator.get(random.randomint(1, int(lengthInput)))
