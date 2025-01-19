#File handling
#write[write(s),writelines(s)]
try:
    with open('file2.txt','w') as f:
        s =input('Enter text here: ')
        f.write(s)
        
except IOError as e:
    print(e)