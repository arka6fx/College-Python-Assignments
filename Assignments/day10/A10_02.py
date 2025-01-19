# A10_02. Write a program to print each line of a file in reverse order.

try:

    file_name = input("Enter the file name: ")

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        print(line.strip()[::-1])  # Strip whitespace and reverse the line

except IOError as e:
    print(e)
