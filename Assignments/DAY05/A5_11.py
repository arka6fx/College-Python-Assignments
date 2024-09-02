#A5_11. write a program to count frequency of all the elements in a tuple.

myTuple = ()
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f'Enter element no. {i + 1}: '))
    myTuple += (element,)


elements = []
frequencies = []


for element in myTuple:
    if element in elements:
        index = elements.index(element)
        frequencies[index] += 1
    else:
        elements.append(element)
        frequencies.append(1)

print("Element frequencies:")
for i in range(len(elements)):
    print(f"Element {elements[i]}: {frequencies[i]}")

