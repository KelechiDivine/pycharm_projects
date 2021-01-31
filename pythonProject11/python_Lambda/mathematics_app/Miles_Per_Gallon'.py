print("Hi, am Drive Technology. I wanna help you with your journey!")
LetUserEnterAnInput = input("Enter Yes to continue with me!: ")

if LetUserEnterAnInput == "Yes":

    InputEnterToContinue = input("Press any key to continue: ")
    UserToEnterGallon = int(input("Enter the input of gallons used: "))
    UserToEnterTheMilesEntered = int(input("Enter the miles covered: "))

    answer = UserToEnterTheMilesEntered / UserToEnterGallon
    print("The tank consumption will be: ", answer)
else:
    print("There was an error while connecting to this server..")

