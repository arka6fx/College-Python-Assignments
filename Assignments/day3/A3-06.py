"""Write a program to find the sum of the even-valued terms of the fibonacci series up to 100."""

limit = int(input("Enter the upper limit for the Fibonacci series: "))


a, b = 0, 1


sum_even = 0

while True:
    
    a, b = b, a + b
    
    if a > limit:
        break

    if a % 2 == 0:
        sum_even += a
    
   
print(f'The sum of the even-valued terms in the Fibonacci series up to {limit} is {sum_even}.')
