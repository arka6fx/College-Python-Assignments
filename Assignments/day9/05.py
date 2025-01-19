#try-except-finally
try:
    x=int(input('x= '))
    y=int(input('y= '))
    z=x/y
    print(z)
except (NameError,ZeroDivisionError,TypeError,ValueError) as e:
    print(e)
finally:
    print('bye')
    
# The code within the finally block is always executed, 
# regardless of whether an exception was raised or not.

# A NameError occurs when you try to use a variable (or function, class, etc.)
# that has not been defined in the current scope.