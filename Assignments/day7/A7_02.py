# A7_02. Write a program to define a function that accepts a string and calculates the 
# number of uppercase letters and lowercase letters.


def count_case_characters(input_string):

    uppercase_count = 0
    lowercase_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


    
user_input = input("Enter a string: ")

uppercase_count, lowercase_count = count_case_characters(user_input)


print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")


