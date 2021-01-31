PromptingAUserToFillThisLine = input("Hi,am Drive technology (press any key to continue)!: ")

rate = 7 / 100
year = 1


principal = int(input("Enter the amount invested: "))

for returns in range(30):
    amount = principal * (1 + rate) ** year

    print(f"{year:>0}\t{amount:.2f}")
    year += 1