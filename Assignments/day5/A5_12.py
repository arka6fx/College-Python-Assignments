#A5_12. write a program to find the distinct pair of 
# numbers whose product is even from a tuple of integers.
myTupple= ()

n = int(input("Enter the number of elements: "))

for i in range(n):
   
    element = int(input(f'Enter element no. {i + 1}: '))
    myTupple += (element,)

evenPairs =()
for i in range(len(myTupple)):
    for j in range(i + 1, len(myTupple)):
        if (myTupple[i] * myTupple[j]) % 2 == 0:
           evenPairs+=((myTupple[i], myTupple[j]),)
print("Even distinct pairs:")
print(evenPairs)
