# A6_06. Write a program to merge two dictionaries.


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


merged_dict = {}

for key in dict1:
    merged_dict[key] = dict1[key]

for key in dict2:
    merged_dict[key] = dict2[key]


print("Merged Dictionary:", merged_dict)
