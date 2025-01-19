#File handling
#write[write(s),writelines(s)]
try:
    with open(r'C:\Users\cseprojectlab\Desktop\Project\file2.txt','a') as f:
        s =['aaaaa\n','bbbbbb\n','cccccc\n']
        f.writelines(s)
        
except IOError as e:
    print(e)