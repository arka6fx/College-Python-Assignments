#Function definition
def math(a,b):
    return a+b, a-b, a*b, a/b

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r1,r2,r3,r4=math(x,y)
print(r1,r2,r3,r4)