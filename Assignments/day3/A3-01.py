"""A3-01. Write a program to check whetehr a given number is a prime or not."""

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False

elif number == 2:
    is_prime = True

elif number % 2 == 0:
    is_prime = False
else:

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            is_prime = False
            break


if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
