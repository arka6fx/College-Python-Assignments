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
print('{0:04.2f}'.format(14.2568697))#also includes point 
# Format String Breakdown:

# {:04.2f}:
# 04 specifies a minimum width of 4 characters, 
# including the decimal point and digits.
# .2f specifies that the number should be formatted as a
# floating-point number with 2 decimal places.

print('{0:06.2f}'.format(14.2568697))