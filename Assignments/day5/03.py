#list aliasing and cloning
# Aliasing means creating an additional reference or 
# name for an existing object in memory.
l1=[10,20,30]
l2=l1
l1[0]=50
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l1=[10,20,30]
l2=l1[::-1]
l1[0]=50
print(l1)
print(l2)
print(id(l1))
print(id(l2))