print("Hi there, am Drive Technology! \n"
      "I'm here to get some info about you...\n\n")

userInputNumber = input("Send 'YES' to continue this process: ")

if userInputNumber == 'YES':
    print("You are good to go! \n\n")

    UserName = input("Please input your name: ")
    UserAge = int(input("Please can you kindly share your age here?: "))
    UserOccupation = input("Can we know about your job?: ")
    UserColor = input("What's your best color?: \n\n")

    print(f"Your name is: {UserName} \n"

          f"You are: {UserAge} years \n"

          f"You are a (an): {UserOccupation} \n"

          f"Your best color(s) is (are): {UserColor} ")

    print(f"Hi {UserName}, It's good having you here!")

    UserEndsTheProgramme = input("Press ENTER KEY to end the programme!: ")

else:
    print("Sorry!! An error occurs while encountering the server.")
