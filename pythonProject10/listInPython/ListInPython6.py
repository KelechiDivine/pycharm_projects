x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y)

thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.remove("apple")
thisTuple = tuple(y)
