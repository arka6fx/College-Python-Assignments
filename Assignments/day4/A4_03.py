'''A4_03)Write a program to get a string from a given string where
all occurences of the last character have been changed to '*', except the last character.'''

s = input('Enter a string: ')

if len(s) == 0:
    print("The string is empty.")
else:
   
    last_char = s[-1] #storing last character
    
    
    result = ''
    for char in s:
        if char == last_char:
            result += '*'
        else:
            result += char
    

   
result = result[0:len(s)-1] + last_char
    
print("Resulting string:", result)

