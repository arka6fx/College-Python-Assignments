#A5_12. write a program to find the distinct pair of 
# numbers whose product is even from a tuple of integers.
myTuple= ()

n = int(input("Enter the number of elements: "))

myTuple = tuple(int(input(f'Enter element no. {i + 1}: ')) for i in range(n))

evenPairs =()
for i in range(len(myTuple)):
    for j in range(i + 1, len(myTuple)):
        if (myTuple[i] * myTuple[j]) % 2 == 0:
           evenPairs+=((myTuple[i], myTuple[j]),)
print("Even distinct pairs:")
print(evenPairs)
