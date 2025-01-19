#File handling
#  with open(file_name, mode, buffer) as f:
try:
    with open('file1.txt') as f:
        print(f.mode)
        print(f.name)
        print(f.closed)
        #access
    print(f.closed)
except IOError as e:
    print(e)