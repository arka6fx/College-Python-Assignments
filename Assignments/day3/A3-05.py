#Write a program that prompts users to enter numbers.This process repeats untill the user enters -1.
#Finally,the program prints the count of prime and composite numbers entered.

prime_count = 0
composite_count = 0

while True:
    
    number = int(input("Enter a number (or -1 to stop): "))
    
    if number == -1:
        break
    
    is_prime = True
    
    if number <= 1:
        is_prime = False
    
    else:
        
        for i in range(2, round(number**0.5) + 1, 1):
            if number % i == 0:
                is_prime = False
                break 

    
    if is_prime:
        prime_count += 1
    elif number > 1:
        composite_count += 1

print(f"Count of prime numbers: {prime_count}")
print(f"Count of composite numbers: {composite_count}")
