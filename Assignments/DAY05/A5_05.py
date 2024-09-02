#A5_05. Write a program to create a list from two given lists 'list1' and  'list2' of numbers
# such that it contains numbers that are present in 'list2' but not in 'list1'.

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

l3=[i for i in l2 if i not in l1]
print(l3)