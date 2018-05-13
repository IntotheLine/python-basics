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
