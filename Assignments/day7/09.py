#map(f,s),reduce(f,s),filter(f,s)
# The map() function takes two main arguments:

# f: A function (or any callable object, including lambda functions).
# s: An iterable (e.g., a list, tuple, string).
# map() applies the function f to each element of the iterable s and
# returns an iterator that yields the results.

l1=[1,2,3,4,5,6]
f=lambda x:x*x
l2=list(map(f,l1))
print(l2)