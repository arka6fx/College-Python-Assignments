#methods
d = {'Math': 98, 'English': 97, 'Sci': 95, 'Math':100}
print(d.keys())
print(d.values())
d = {'Math': 98, 'English': 97, 'Sci': 95}
print(d.items()) #list of tuple containing key and value pair
#dictionary inversion
d1={v:k for k,v in d.items()}
print(d)
print(d1)