d = {'Math': 98, 'English': 97, 'Sci': 95}
d1={v:k for k,v in d.items()}
print(sum(d1))
del d #deletes the dictionary i.e the object
d = {'Math': 98, 'English': 97, 'Sci': 95}
print(d.get('Math'))
d2=d.copy()#cloning
d['Math']=100
print(d)
print(d2)