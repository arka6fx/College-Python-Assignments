'''list(mutable) and tuple(immutable)'''
l=[]
print(type(l))
l1=[10,23,34]
len(l1)
t=()
type(t)
t1=(10)
type(t1)
t1=(1,)
type(t1)
t2=(1,2,3)
l2=list(t2)
print(l2[::-1])

#list aliasing and cloning
l1=[10,20,30]
l2=l1
l1[0]=50
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l2=l1[::-1]
l1[0]=50
print(l1)
print(l2)
print(id(l1))
print(id(l2))
#list comprehension
l=[x for x in range(1,10) if x%2==0]
print(l)

[print(i,end=' ') for i in l]
print()
l3=[10,20,30]
l4=[40,50,60]
print(l3+l4)
print(l3*3)
print(20 in l3)
print(20 in l4)

t3=[10,20,30]
t4=[40,50,60]
print(t3+t4)
print(t3*3)
print(20 in t3)
print(20 in t4)

#methods

#l.append(i)  not applicable for tuple
l5=[10,20,30]
l5.append(60)
print(l5)

l=[]
for i in range(1,10):
    l.append(i)

print(l)

#l.extend(l1) not applicable for tuple
l1=[10,20,30]
l2=[60,70]
print(l1)
print(l2)
l1.extend(l2)
print(l1)
print(l2)

#l.count() applicable for tuple
l1=[10,20,30,10,20]
print(l1.count(20))
print(l1.count(0))

#l.index()
l1=[10,20,30,40,50]
print(l1.index(20))
# print(l1.index(0))

#l.remove(i)
l1=[10,20,30,40,50]

l1.remove(20)
print(l1)
l1.pop() #not applicable for tuple
l1=[10,20,30]
print(l1)
l1.insert(0,50) #not applicable for tuple
l1=[10,20,30]
print(l1)

del l1[1] #not applicable for tuple
l1=[10,20,30]
print(l1)

l1.clear() #remove the elements and make it empty
print(l1)

del l1   #object will be deleted
#print(l1)

t=(10,20)
# del t[0] # will not work

del t # will work

l1=[10,50,30]
l1.sort
print(l1)

print(sorted(l1)) # also works for tuple (as it will not access the object)

print(l1)

l1.reverse
t=tuple(l1)
sorted(t)

print(min(l1))
print(max(l1))
print(sum(l1))

t=(10,20,30,40)
print(min(t))
print(max(t))
print(sum(t))

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