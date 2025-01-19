#try-except-else
try:
    x=int(input('x= '))
    y=int(input('y= '))
    z=x/y
except (ZeroDivisionError,TypeError,ValueError) as e:
    print(e)
else:
    print(z)
  
#The else block is executed only if no exception is raised in the try block. 
# This is the key function of the else clause. 
# It allows you to separate the code that should only run if the try block completes 
# successfully from the code that handles exceptions.    