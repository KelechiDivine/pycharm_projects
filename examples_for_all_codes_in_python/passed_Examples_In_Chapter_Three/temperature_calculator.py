from utils import add, multiplication


def covert(celcius):
    fahrenheit = multiplication(celcius, 1.8)
    return add(fahrenheit, 32)


User = input(" Enter Number that's separated by comma: ")
print("User_Input", User)

User1 = User.split()
print("User_Input1", User1)

for User in range(1, 10):
    User_Input = int(User)
    temperature = covert(User_Input)

    print(f"The temperature is {covert(User)}")
