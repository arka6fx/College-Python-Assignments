# A6_05. Write a program to sort (ascending order) a dictionary by value.

my_dict = {'apple': 4, 'banana': 2, 'cherry': 5, 'date': 3}


items = list(my_dict.items())
print(items)
n = len(items)
for i in range(1,n): #no. of passes
    for j in range(1, n-i+1):
        if items[j-1][1] > items[j][1]:
            items[j-1], items[j] = items[j], items[j-1]

sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value


print("Sorted Dictionary (by value in ascending order):", sorted_dict)
