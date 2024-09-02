
l1=[1,2,3,4]
l2=[3,4,5,6]

l3=[]
for element in l1:
    if element not in l3:
        l3.append(element)
for element in l2:
    if element not in l3:
        l3.append(element)

print(l3)