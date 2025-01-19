# A10_02. Write a program to print each line of a file in reverse order.

try:

    file_name = input("Enter the file name: ")

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        print(line.strip()[::-1])  # Strip whitespace and reverse the line

except FileNotFoundError:
    print("Error: The file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
