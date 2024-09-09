# A6_05. Write a program to sort (ascending order) a dictionary by value.

my_dict = {'apple': 4, 'banana': 2, 'cherry': 5, 'date': 3}


items = list(my_dict.items())
n = len(items)
for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value


print("Sorted Dictionary (by value in ascending order):", sorted_dict)
