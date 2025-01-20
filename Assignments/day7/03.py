#Parameters and arguments
#Positional

#Function definition
def math(a,b):
    return a+b, a-b, a*b, a/b

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r=math(y,x)
print(r)