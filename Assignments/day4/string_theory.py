#Data Structure or Data Type
#String -->ordered sequence of characters and is immutable
s='This is \x61\x6e  \nexample'
print(s)
#Raw String  --> prints escape sequence characters normally
s=r'This is \x61\x6e  \nexample'
print(s)
# % and format() <---formating string--->
print('%s has scored %d in maths' %('Ronit',98))
print('{} has scored {} in math'.format('Ronit',98))
print('{1} has scored {0} in math'.format('Ronit',98))# change order
print('{m} has scored {n} in math'.format(n='Ronit',m=98))
print('1/3 is {0:.4f}'.format(1/3))
print('{:04.2f}'.format(14.2568697))#also includes point 
print('{:06.2f}'.format(14.2568697))

# String Index --> access single character
s='python'
print(s[0])
#String Slice  --->access multiple character
print(s[0:3:2])#[start:stop:step]
print(s[0::2])
print(s[::])
print(s[::-1])
s1 = s[::-1]#reverse string
if s == s1:
    print('Palindrome')
#concatenate string t and y
t='ar'
y='ka'
print(t+y)
#string repetition
print(t*3)
for i in  range (len(s)):
    print(s[i],end='')
#Module/function-->makes the code modular and less repition of code
#object.method()
    
#max()
str='python'
print('\n',max(s)) # y has highest ascii value in python
#find(str,start,end)
s='python programming language'
print(s.find('tho'))#--> returns first occurence index
print(s.find('n',4,10))
#count(str,start,end)
print(s.count('n',0,26))
print(s.replace('n','**',2)) #max=2(count)  replace first two n by **
print(s.replace('n','**',0))
#upper()
print(s.upper())
#lower()
print(s.lower())
#strip()
print(s.strip())
#split(str,num)   here, num specifies number of splits and str specifies where split will occur
s='python program'
print(s.split())#returns list of two items ['python', 'program']
s2='11 ,12 , 13'
print(s2.split(',',2))
print(s2.split(' ',2))
print(s.split('h',2))
#str.join(seq)
s=['python','program']
print(''.join(s)) # creats object
print('%^&'.join(s))
s4=['11','12','13']
print('+'.join(s4))



























































































