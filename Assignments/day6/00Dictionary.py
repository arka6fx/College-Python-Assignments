#Dictionaries
#(just like structure in c)
#unordered sequence of elemnts
#key:value pair
d = {'Math': 98, 'English': 97, 'Sci': 95}
len(d)
print(d)
 
#orddict
d = {'Math': 98, 'English': 97, 'Sci': 95}
#print(d['math'])

#dictionary(value) is mutable but dictionary key is unmutable and is unique
d = {'Math': 98, 'English': 97, 'Sci': 95, 'Math':100}
#methods
print(d.keys())
print(d.values())
d = {'Math': 98, 'English': 97, 'Sci': 95}
print(d.items()) #list of tuple containing key and value pair
#dictionary inversion
d1={v:k for k,v in d.items()}
print(d)
print(d1)
d = {'Math': 98, 'English': 97, 'Sci': 95}
print(d.pop('Math')) #return value
print(d)
d = {'Math': 98, 'English': 97, 'Sci': 95}
print(d.popitem()) # will delete any arbitrary item #returns item
print(d)
d = {'Math': 98, 'English': 97, 'Sci': 95}
print(max(d)) #print key with max ascii value
print(min(d)) #print key with min ascii value

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
