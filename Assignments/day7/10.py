#map(f,s),reduce(f,s),filter(f,s)
# The filter() function takes two arguments:

# f: A function (or any callable object, like a lambda function) 
# that returns a boolean value (True or False).
# s: An iterable (e.g., a list, tuple, string).
# filter() applies the function f to each element of the iterable s.
# It keeps only the elements for which f returns True and discards 
# the elements for which f returns False. It returns an iterator 
# that yields the filtered elements.

l1=[1,2,3,4,5,6]
f=lambda x:x%2 == 0
l2=list(filter(f,l1))
print(l2)