#3. from module_name import function_name(s)
#function_name
from calculator import add,mul
x=int(input('x= '))
y=int(input('y= '))
z = add(x,y)
z1 = mul(x,y)
print(z, z1)