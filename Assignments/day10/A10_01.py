# 11/12/24 A10_01. Write a program to accept a file name from the user and 
# count the number of words present in the file.


try:

    file_name = input("Enter the file name: ")
    
    with open(file_name, 'r') as file:
        content = file.read()
        
    words = content.split()  # Split content into words
    word_count = len(words)

    print(f"The number of words in the file '{file_name}' is: {word_count}")


except FileNotFoundError:
    print("Error: The file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
