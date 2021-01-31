from maximum_app import maximum , minimum

number = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

int_max = maximum(number, number2, number3)
int_min = minimum(number, number2, number3)
print(int_min)
print(int_max)
