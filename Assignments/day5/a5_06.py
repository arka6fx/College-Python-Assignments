l1 = [1, 2, 3, 4]
odd_product = []

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] % 2 == 1 and l1[j] % 2 == 1:
            #product = l1[i] * l1[j]
            odd_product.append((l1[i],l1[j]))

print(odd_product)

     


