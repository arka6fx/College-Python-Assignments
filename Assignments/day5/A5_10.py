#A5_10. write a program to display unique and duplicate elements of a tuple.


myTuple = ()

n = int(input("Enter the number of elements: "))
myTuple = tuple(int(input(f'Enter element no. {i + 1}: ')) for i in range(n))


unique_elements = []
duplicate_elements = []

seen_elements = []


for element in myTuple:
    if element in seen_elements:
        if element not in duplicate_elements:
            duplicate_elements.append(element)
    else:
        seen_elements.append(element)

final_unique_elements = [element for element in seen_elements if element not in duplicate_elements]

print("Unique elements:", final_unique_elements)
print("Duplicate elements:", duplicate_elements)


