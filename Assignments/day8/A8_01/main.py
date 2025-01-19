# 25/11/24 A8_01. Create a module to check if a passed string is a palindrome or not. 
# Write a program to find whether a string is a palindrome or not using this module.

import palindrome

str = input('Enter a string: ')

if palindrome.check_palindrome(str):
    print("The string is a palindrome!")
else:
    print("The string is NOT a palindrome!")