#Parameters and arguments
#variable length arguments

# *v: This is the key part. The * before the parameter name v 
# indicates that the function can accept a variable number of 
# positional arguments. All the arguments passed to the function 
# will be collected into a tuple named v inside the function.

#Function definition
def math(*v):
    s=0
    for i in v:
        s+=i
    return s

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
z=int(input('Enter value of z:'))
r=math(x,y,z,4,5,6)
print(r)


