#assign a value to each key
d = {}
s = 'python'
value = 1

for i in s:
    d.setdefault(i, value)
    value += 1  # Increment the value for the next key

print(d)

l=[10,20,30,40]
d=dict.fromkeys(l,'Math')
print(d)

l=[10,20,30,40]
l1=[1,2,3,4]
d=dict.fromkeys(l,l1)
print(d)