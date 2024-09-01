#A4_06) Write a program to detect whether two strings are anagrams or not.

str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')


str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()


if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
