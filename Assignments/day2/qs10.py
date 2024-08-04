principle = float(input("Enter the principle amount: "))
time = float(input("Enter the time period: "))

if principle < 200000:
    rate = 10
elif principle >= 200000 and principle <= 1000000:
    rate = 12
else:
    rate = 15

simple_interest = (principle * rate * time)/100
print("Simple Interest:", simple_interest)
