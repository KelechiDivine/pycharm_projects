name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

z = zip(name, animal, age)

name. append('Nzynger')
animal.append('dog')
age. append(5)

for name, animal, age in z:
    print("%s the %s is %s" % (name, animal, age))



