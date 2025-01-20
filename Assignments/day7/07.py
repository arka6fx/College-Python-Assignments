#Parameters and arguments
#variable length arguments

#Function definition
def check(z):
    global x
    x+=5
    z-=2
    print('Inside the function',x,y,z)     

# global x: This line inside the check function declares that 
# the x being used within the function is the global x defined 
# outside the function. Without this declaration, x inside the 
# function would be treated as a local variable.

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
z=int(input('Enter value of z:'))
print('Before function call',x,y,z)
check(z)
y+=4
print('After function call',x,y,z)