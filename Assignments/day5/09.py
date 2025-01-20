l1=[10,20,30,40,50]

del l1[1] #not applicable for tuple
print(l1[1])
l1=[10,20,30]
print(l1)


l1.clear() #remove the elements and make it empty
print(l1)

del l1   #object will be deleted
#print(l1)

t=(10,20)
# del t[0] # will not work

del t # will work