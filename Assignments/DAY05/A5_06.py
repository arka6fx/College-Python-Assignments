#A5_06. Write a program to find the distinct pair of numbers
# whose product is odd from a list of integers.
l1= []
n = int(input("Enter the no. of elements: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    l1.append(element)

oddPairs = []

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if (l1[i] * l1[j])% 2 == 1:
            oddPairs.append((l1[i],l1[j]))

print("Odd distinct pairs:")
print(oddPairs)

     


