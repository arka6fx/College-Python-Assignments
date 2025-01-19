# A10_04. Write a program to copy the first 100 characters of a binary file into another.


try:
    source_file = input("Enter the source binary file name: ")
    destination_file = input("Enter the destination binary file name: ")
    

    with open(source_file, 'rb') as src:
        data = src.read(100)  # Read the first 100 bytes
    

    with open(destination_file, 'wb') as dest:
        dest.write(data)
    

    print(f"The first 100 characters have been copied to '{destination_file}' successfully.")


except FileNotFoundError:
    print("Error: The source file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
