#File handling
# f =open(file_name, mode, buffer)
try:
    f= open('file1.txt')
    print(f.mode)
    print(f.name)
    print(f.closed)
    #access
    f.close()
    print(f.closed)
except IOError as e:
    print(e)