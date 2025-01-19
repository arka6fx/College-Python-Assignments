#function
'''
int add(int a, int b){
c= a+b
return c
}'''
#Function definition
def add(a,b):
    c=a+b
    return c

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r=add(x,y)
print(r)

#Function definition
def math(a,b):
    return a+b, a-b, a*b, a/b

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r1,r2,r3,r4=math(x,y)
print(r1,r2,r3,r4)


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

#Lambda function/inline function
#Syntax: lambda arguments:expression

#Function definition
a=lambda a,b:a+b
m=lambda a,b:a*b
#Function call
r=a(10,5)
r1=m(10,5)
print(r,r1)

#map(f,s),reduce(f,s),filter(f,s)
# The map() function takes two main arguments:

# f: A function (or any callable object, including lambda functions).
# s: An iterable (e.g., a list, tuple, string).
# map() applies the function f to each element of the iterable s and
# returns an iterator that yields the results.

l1=[1,2,3,4,5,6]
f=lambda x:x*x
l2=list(map(f,l1))
print(l2)

#map(f,s),reduce(f,s),filter(f,s)
# The filter() function takes two arguments:

# f: A function (or any callable object, like a lambda function) 
# that returns a boolean value (True or False).
# s: An iterable (e.g., a list, tuple, string).
# filter() applies the function f to each element of the iterable s.
# It keeps only the elements for which f returns True and discards 
# the elements for which f returns False. It returns an iterator 
# that yields the filtered elements.

l1=[1,2,3,4,5,6]
f=lambda x:x%2 == 0
l2=list(filter(f,l1))
print(l2)

#map(f,s),reduce(f,s),filter(f,s)
from functools import reduce
l1=[1,2,3,4,5,6]
f=lambda x,y:x+y
r=reduce(f,l1)
print(r)

# reduce() takes the first two elements of l1 (1 and 2) and applies f to them: f(1, 2) returns 1 + 2 = 3.

# reduce() then takes the result of the previous step (3) and the next element of l1 (3) and applies f again: f(3, 3) returns 3 + 3 = 6.

# This process continues:

# f(6, 4) returns 6 + 4 = 10
# f(10, 5) returns 10 + 5 = 15
# f(15, 6) returns 15 + 6 = 21
# Finally, reduce() returns the single accumulated value, which is 21.
'''
[1,2,3,4,5,6]
[2,3,4,5,6]
[6,4,5,6]
[24,5,6]
[120,6]
720
'''