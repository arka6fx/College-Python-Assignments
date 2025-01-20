# UNPACKING  SAME FOR TUPLE
l1=[2,3,5]
x,y,z=l1
print(x)
print(y)
print(z)

x, *y=l1
print(x)
print(y)

#packing

a=2
b=4
c=5

l3=[a,b,c]
print(l3)