#list comprehension
# [expression for item in iterable if condition]

l=[2*x for x in range(1,10) if x%2==0 ]
print(l)

[print(i,end=' ') for i in l]
print()
l3=[10,20,30]
l4=[40,50,60]
print(l3+l4)
print(l3*3)
print(20 in l3)
print(20 in l4)

t3=(10,20,30)
t4=(40,50,60)
print(t3+t4)
print(t3*3)
print(20 in t3)
print(20 in t4)