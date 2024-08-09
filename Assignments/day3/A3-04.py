#Write a program to find the sum of all prime numbers within a given range.

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum_of_primes = 0
for number in range(start, end + 1):
    is_prime = True

    if number <= 1:
        is_prime = False
    
    else:
       
        for i in range(2,round(number ** 0.5) + 1, 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        sum_of_primes += number

print(f'''The sum of all prime numbers between {start} and 
      {end} is {sum_of_primes}.''')

