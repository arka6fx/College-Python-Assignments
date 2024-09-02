
my_tuple = (1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 5)

counts = {}
duplicates = set()
uniques = set()

for item in my_tuple:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for item, count in counts.items():
    if count > 1:
        duplicates.add(item)
    else:
        uniques.add(item)

duplicates_list = sorted(list(duplicates))
uniques_list = sorted(list(uniques))

print("Unique elements:", uniques_list)
print("Duplicate elements:", duplicates_list)
