#5. from module_name import function_name as new_function_name
#new_function_name
from calculator import add as a
from calculator import mul as m
x=int(input('x= '))
y=int(input('y= '))
z = a(x,y)
z1 = m(x,y)
print(z, z1)