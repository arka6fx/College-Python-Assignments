my_tuple = (1, 2, 3, 4, 5, 6)

pairs = set()
for i in range(len(my_tuple)):
    for j in range(i + 1, len(my_tuple)):
        if (my_tuple[i] * my_tuple[j]) % 2 == 0:
            pairs.add((my_tuple[i], my_tuple[j]))

for pair in pairs:
    print(pair)
