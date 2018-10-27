# FAQ Lists and Index and Methods.py

# ListMethods.py

spam = ['Dog', 'tail', 'gin', 'vodka']
spam.index('tail')
# output = 1, because lists start always with index 0

# Work with Lists, append / insert / remove / del
spam.append('tonic water')  # adds tonic water to the list
spam.insert(1, 'white russian')  # new list: dog, white russian, tail, gin, vodka, tonic water
spam.remove('gin')  # removes gin from the list, always the first value in a hole list

del spam[0]  # deletes dog because it has the aligned index 0

# Sort Lists, lists with strings and integers can not be sorted
spam.sort()  # sorts the list numeric or alphabetical
spam.sort(reverse=True)  # sorts the list reverse wether numbers or alpharbeticals
spam.sort(key=str.lower)  # sorts in true alphabetical order, otherwhise all caps are beyond small written letters

###
###
###

# ForLoopsinLists

range(4)
print(range(4))

list(range(4))
list(range(0, 100, 2))

spam = list(range(0, 100, 2))
print(spam)

supplies = ['Vine', 'Gin', 'Tonic', 'Sparkling Water', 'Lemon', 'Vodka']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' on stock ' + supplies[i])

###
###
###

# Augmented assignment statement == Equivalent assignment statement

spam += 1 == (spam=spam + 1)
spam -= 1 == (spam=spam - 1)
spam *= 1 == (spam=spam * 1)
spam /= 1 == (spam=spam / 1)
spam %= 1 == (spam=spam % 1)

spam = 42
spam = spam + 1  # oder spam += 1
spam += 1

['cat', 'bat', 'rat', 'elephant']
# items are comma seperated, and in claws
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
# shows 'cat', list starts at 0
spam = [['cat', 'bat', ], [10, 20, 30, 40, 50, ]]

spam = 'hello'
spam

spam = [10, 20, 30]
# ersetzt die 20 durch hello, Liste startet bei 0 ist Zahltechnisch 1
spam[1] = 'hello'
spam
# folgendes ersetzt 20;30, Liste hat dann 4 Items
spam[1:3] = ['Hund', 'Katze', 'Maus']
spam

name = ['rita', 'Marita', 'Marta'
        'Elisa']
del name[2]  # marita == deleted

# output variationen

name = ['rita', 'Marita', 'Marta', 'Elisa']
name[:2]
# output = ['Rita', 'Marita'], weil bis 2 wird ausgespuckt, Also Wert 0 + 1

name = ['rita', 'Marita', 'Marta', 'Elisa']
name[1:]
# output = alles ab wert 1 also Marita

name = [1, 2, 3, 4]
if str(1) in name == True
    print('Well Done')
