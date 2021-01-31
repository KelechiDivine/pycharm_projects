thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

thisList2 = ["apple", "banana", "cherry",]
thisList2.pop(0)
print(thisList2)

thisList3 = ["apple", "banana", "cherry"]
thisList3.pop()
print(thisList3)

thisList4 = ["apple", "banana", "cherry"]
del thisList4

thisList5 = ["apple", "banana", "cherry"]
thisList5.clear()
print(thisList5)

thisList6 = ["apple", "banana", "cherry",]
for x in thisList6:
    print( x )

thisList7 = ["SurName: " "Okoroafor", "First Name:" " Kelechi", "Middle Name: " "Divine",
             "Age: " "19 years", "Education: " "A student at semicolon village Africa as a Software Engineer!"]
for x in thisList7:
    print(x)

# print(thisList7["SurName"])