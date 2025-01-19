#if condition:
#   raise Exception(message)
try:
    x=int(input('x= '))
    y=int(input('y= '))
    if y == 0:
        raise ZeroDivisionError('Zero division not allowed')
except ZeroDivisionError as e:
    print(e)
else:
    z=x/y
    print(z)
    
