#A4_02) Write a program to read a string and check whether the string is a palindrome or not.
str = input('Enter a string: ')
rev_str =  str[::-1]
if str == rev_str:
    print('palindrome')
else:
    print('Not Palindrome')

            
