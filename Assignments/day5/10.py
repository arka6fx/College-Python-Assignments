# sort(): This method sorts the list in place.
l1 = [10, 60, 30]
l1.sort()  # Correct: Call the sort() method with parentheses
print(l1)  # Output: [10, 30, 60]

l2 = [10, 50, 30]
# sorted(): This function returns a new sorted list.
print(sorted(l2))  # Output: [10, 30, 50]
print(l2) #Output: [10, 50, 30]

t1 = (20,10,30)
print(sorted(t1)) #Output: [10, 20, 30]
print(t1) #Output: (20, 10, 30)