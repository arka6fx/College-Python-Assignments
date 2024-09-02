#A5_03 Write a program to find the union of two lists.
l1= []
n = int(input("Enter the no. of elements: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    l1.append(element)


l2= []
m = int(input("Enter the no. of elements: "))
print("Enter the elements: ")
for j in range (m):
    element = int(input(f'Enter element no. {j+1} : '))
    l2.append(element)

union = l1[:]

for element in l2:
    if element not in union:
        union.append(element)

print(union)