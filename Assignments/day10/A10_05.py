# A10_05. Write a program to copy the content of the text file to 
# another file by converting all lowercase characters to uppercase.


try:

    source_file = input("Enter the source text file name: ")
    destination_file = input("Enter the destination text file name: ")

    with open(source_file, 'r') as src:
        content = src.read()
    

    uppercase_content = content.upper()
    

    with open(destination_file, 'w') as dest:
        dest.write(uppercase_content)

    print(f"Content has been copied to '{destination_file}' with all lowercase letters converted to uppercase.")

except FileNotFoundError:
    print("Error: The source file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
