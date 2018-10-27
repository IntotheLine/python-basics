# random password generator.py
import random

a = "a"
b = "b"
c = "c"
d = "d"
e = "e"

generator = {1: a, 2: b, 3: c, 4: d, 5: e}
random = random.randint(1, 5)
pw = generator.get(random)
print(pw)
