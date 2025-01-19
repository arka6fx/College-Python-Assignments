# A10_06.  Write a program to copy one Python script into another in such a
# way that all comment lines are skipped and not copied to the destination file.


try:

    source_file = input("Enter the source Python script name: ")
    destination_file = input("Enter the destination Python script name: ")
    
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        for line in src:
            stripped_line = line.strip()
            if not stripped_line.startswith("#") and stripped_line != "":
                dest.write(line)  # Write non-comment lines to the destination file
    

    print(f"The content of '{source_file}' has been copied to '{destination_file}' without comments.")


except FileNotFoundError:
    print("Error: The source file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
