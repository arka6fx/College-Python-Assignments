my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)

counts = {}
for item in my_tuple:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for item, count in counts.items():
    print(f"{item}: {count}")
