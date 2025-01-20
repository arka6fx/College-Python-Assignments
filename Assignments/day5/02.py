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