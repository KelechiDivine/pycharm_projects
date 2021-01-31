thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

thisList2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList2[1:3] = ["blackcurrant", "watermelon"]
print(thisList2)

thisList3 = ["apple", "banana", "cherry"]
thisList3.insert(2, "watermelon")
print(thisList3)

thisList4 = ["apple", "banana", "cherry"]
thisList4.append("orange")
print(thisList4)

thisList5 = ["apple", "banana", "cherry"]
thisList5.insert(1, "orange")

thisList6 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList6.extend(tropical)
print(thisList6)

thisList7 = ["Name:", "Phone Number:", "age/date of birth:"]
tropical2 = ["Okoroafor Kelechi Divine", "08082167764", "December 16th"]
thisList7.extend(tropical2)
print(thisList7)