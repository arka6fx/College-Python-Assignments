# A10_03. Write a program to reverse the content of a file and store it in another file.


try:

    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    with open(source_file, 'r') as file:
        content = file.read()
    
    reversed_content = content[::-1]
    

    with open(destination_file, 'w') as file:
        file.write(reversed_content)
    
    print(f"Content reversed and stored in '{destination_file}' successfully.")


except FileNotFoundError:
    print("Error: The source file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
