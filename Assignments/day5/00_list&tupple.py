'''list(mutable)'''

# In Python, a list is a mutable, ordered sequence of items. 
# Lists can hold elements of different data types (integers, strings, floats, etc.),
# and you can modify their contents after creation.
# Key Features of a List:
# Mutable: You can modify lists (e.g., add, remove, or change items).
# Ordered: The items in a list maintain the order in which they were added.
# Dynamic: Lists can grow or shrink in size.

''' tuple(immutable)'''
# A tuple in Python is a data structure that is similar to a list but immutable. 
# Once a tuple is created, its elements cannot be changed, added, or removed.
# Tuples are typically used to store collections of items that should not be modified.

# Key Features of a Tuple:
# Immutable: You cannot modify the contents of a tuple after its creation.
# Ordered: Tuples maintain the order of elements.
# Allows duplicates: Tuples can contain duplicate values.
# Can store multiple data types: Tuples can hold items of different data types like integers, strings, floats, etc.
l=[]
print(type(l))
l1=[10,23,34]
len(l1)
t=()
print(type(t))
t1=(10)
print(type(t1))
t1=(1,)
print(type(t1))
t2=(1,2,3)
l2=list(t2)
print(l2[::-1]) #reversing using slicing

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

l2=l1[::-1]
l1[0]=50
print(l1)
print(l2)
print(id(l1))
print(id(l2))

#list comprehension
# [expression for item in iterable if condition]

l=[2*x for x in range(1,10) if x%2==0]
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

#l.index() applicable for tuple
l1=[10,20,30,40,50]
print(l1.index(20))



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

# sort(): This method sorts the list in place. It modifies the original list and does not return a new list.
l1=[10,50,30]
l1.sort
print(l1)
# sorted(): This function returns a new sorted list and does not modify the original list.
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