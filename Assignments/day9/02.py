#try-except exception class
try:
    x=int(input('x= '))
    y=int(input('y= '))
    z=x/y
    print(z)
except ZeroDivisionError as e:
    print(e)
except TypeError as e1:
    print(e1)
except ValueError as e2:
    print(e2)
    
    
# TypeError: A TypeError occurs when you try to perform an 
# operation on an object of an inappropriate type. 
# For example, trying to add a string to an integer ("hello" + 5) 
# would raise a TypeError.    

# ValueError: A ValueError occurs when you pass an argument of the correct type to a function, 
# but the argument has an inappropriate value. In your case, int() expects a string that represents an integer.
# The string '7.8' represents a floating-point number, not an integer. 
# Therefore, int('7.8') raises a ValueError.