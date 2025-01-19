#Module/function-->makes the code modular and less repetition of code
#object.method()
#max()
s='python'
print('\n',max(s)) # y has highest ascii value in python
#find(str,start,end)
s='python programming language'
print(s.find('tho'))#--> returns first occurence index
print(s.find('n',4,10))
#count(str,start,end)
print(s.count('n',0,26))
print(s.replace('n','**',2)) #max=2(count)  replace first two n by **
print(s.replace('n','**',0))