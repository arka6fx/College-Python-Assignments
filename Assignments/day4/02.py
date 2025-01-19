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