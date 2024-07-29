principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period: "))

if principal < 200000:
    rate = 10
elif principal >= 200000 and principal <= 1000000:
    rate = 12
else:
    rate = 15

simple_interest = (principal * rate * time)/100
print("Simple Interest:", simple_interest)
