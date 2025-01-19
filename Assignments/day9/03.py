#try-except exception class
try:
    x=int(input('x= '))
    y=int(input('y= '))
    z=x/y
    print(z)
except (ZeroDivisionError,TypeError,ValueError) as e:
    print(e)
