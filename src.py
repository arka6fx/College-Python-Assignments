#File handling
#Reading[read(size),readline(size),readlines(size)]
try:
    with open('file1.txt') as f:
        fc=f.read(10)
    print(fc)
        
except IOError as e:
    print(e)