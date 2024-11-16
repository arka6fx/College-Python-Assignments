file_path = r"C:\Users\arkag\Downloads\Ae Expressions\text expression.txt"
file = open(file_path, 'r')
content = file.read()
print("File contents:")
print(content)
file.close()