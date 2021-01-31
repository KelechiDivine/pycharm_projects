fruit = ("apple", "banana", "cherry")
(green, yellow, red) = fruit
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry",
         "strawberry", "raspberry")
(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)


fruiting = ("apple", "mango", "papaya",
            "cherry", "pineapple")
(green, *tropic, red) = fruiting
print(green)
print(tropic)
print(red)