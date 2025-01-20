d = {'Math': 98, 'English': 97, 'Sci': 95}
d1={v:k for k,v in d.items()}
print(d)
print(d1)
d.update(d1) #appends d1 to d
print(d)
d = {'Math': 98, 'English': 97, 'Sci': 95}
d.setdefault('Geo')
print(d)
d['Geo']=90
print(d)
d={}
l=[10,20,30,40]
for i in l :
    d.setdefault(i)
print(d)
d={}
s='python'
for i in s :
    d.setdefault(i)
print(d)
