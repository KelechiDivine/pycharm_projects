userToEnterFirstInteger = int(input("Enter an first Integer: "))
userToEnterSecondInteger = int(input("Enter second Integer: "))
userToEnterThirdInteger = int(input("Enter third Integer: "))

if userToEnterFirstInteger > userToEnterSecondInteger and \
        userToEnterFirstInteger > userToEnterThirdInteger:

    largestNumber = userToEnterFirstInteger

elif userToEnterSecondInteger > userToEnterFirstInteger and \
        userToEnterSecondInteger > userToEnterThirdInteger:

    largestNumber = userToEnterSecondInteger

else:
    largestNumber = userToEnterThirdInteger

print("The largest Number is:", largestNumber)

if userToEnterFirstInteger < userToEnterSecondInteger and \
        userToEnterFirstInteger < userToEnterThirdInteger:

    smallestNumber = userToEnterFirstInteger

elif userToEnterSecondInteger < userToEnterFirstInteger and \
        userToEnterSecondInteger < userToEnterThirdInteger:

    smallestNumber = userToEnterSecondInteger

else:
    smallestNumber = userToEnterThirdInteger

print("The smallest Number is: ", smallestNumber)


addition = userToEnterFirstInteger + userToEnterSecondInteger + userToEnterThirdInteger

products = (userToEnterFirstInteger * userToEnterSecondInteger * userToEnterThirdInteger)

average = (addition) / 2
