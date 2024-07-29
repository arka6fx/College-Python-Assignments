name = "Arka" # string is immutable
length =  len(name)
print(length)
#slicing
nameshort = name[0:2] #start from index 0 all the way till 2 (excluding 2)
print(nameshort)
character1 = name[1]
print(character1)
print(name[-3:-1])
print(name[1:3])
print(name[:3]) #0:3
print(name[1:]) #1:4(lenght of string)
print(name[1:4])
#slicing with skip value
print(name[0:4:2])