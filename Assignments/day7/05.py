#Parameters and arguments
#default

# b=2: This sets a default value of 2 for the parameter b. 
# This means that if the function is called without explicitly 
# providing a value for b, it will automatically use the default 
# value of 2.

#Function definition
def math(a,b=2):
    return a+b, a-b, a*b, a/b

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r=math(x)
print(r)