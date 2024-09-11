#Data Structure or Data Type
#String -->ordered sequence of characters and is immutable

# Characteristics:
# Ordered
# Immutable (cannot be changed after creation)
# Indexed by position

# The prefix \x indicates that what follows is a hexadecimal value.
# 61 is a hexadecimal number where each digit represents a power of 16.


s='This is \x61\x6e \nexample'
print(s)
#Raw String  --> prints escape sequence characters normally
# In Python, a raw string literal is a way to define a string where 
# backslashes (\) are treated as literal characters and not as escape 
# characters. This is useful for regular expressions, file paths, and 
# other scenarios where backslashes are commonly used and you want to 
# avoid the complexity of escaping them.

s=r'This is \x61\x6e  \nexample'
print(s)
# % and format() <---formating string--->
print('%s has scored %d in maths' %('Ronit',98))
print('{} has scored {} in math'.format('Ronit',98))
print('{1} has scored {0} in math'.format('Ronit',98))# change order
print('{m} has scored {n} in math'.format(n='Ronit',m=98))
print('1/3 is {0:.4f}'.format(1/3))
print('{:04.2f}'.format(14.2568697))#also includes point 
# Format String Breakdown:

# {:04.2f}:
# 04 specifies a minimum width of 4 characters, 
# including the decimal point and digits.
# .2f specifies that the number should be formatted as a
# floating-point number with 2 decimal places.

print('{:06.2f}'.format(14.2568697))

# String Index --> access single character
s='python'
print(s[0])
#String Slice  --->access multiple character
print(s[0:3:2])#[start:stop:step]
print(s[0::2])
print(s[::])
print(s[::-1])
#When using a negative step, the start index should be greater than the stop index for the slicing to produce a result.
print(s[4:2:-1])
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
#Module/function-->makes the code modular and less repitition of code
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
s = "***Hello, World!***"
stripped_s = s.strip('*')
print(f"'{stripped_s}'")  # Output: 'Hello, World!'
#split(str,num)   here, num specifies number of splits and str specifies where split will occur
#splits str into list elements
s='python program'
print(s.split())#returns list of two items ['python', 'program']
s2='11 ,12 , 13'
# Splitting by a Specific Separator:
print(s2.split(',',2))
# Splitting by Whitespace:
print(s2.split(' ',2))
print(s.split('h',2))
#str.join(seq)  joins lists , tuples
s=['python','program']
print(''.join(s)) # creats object
fruits = ['apple', 'banana', 'cherry']
fruit_list = ', '.join(fruits)
print(fruit_list)  # Output: 'apple, banana, cherry'
print('%^&'.join(s))
s4=['11','12','13']
print('+'.join(s4))




str = "i am studying python from ApnaCollege"
str = str.capitalize()
print()
print(str)























































































