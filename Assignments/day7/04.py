#Parameters and arguments
#keyword

# a=x, b=y: These are keyword arguments. 
# They explicitly associate the values of x and y with the 
# corresponding parameters a and b in the function definition. 
# This makes the code more readable, especially when the function 
# has many parameters.

#Function definition
def math(a,b):
    return a+b, a-b, a*b, a/b

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r=math(a=x,b=y)
print(r)