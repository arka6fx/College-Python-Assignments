n = 5  # Number of rows

num = 1
for i in range(n):
    for j in range(i):
        if j==i-1:
            print(num,end="")
        else:
            print(num,end=",") 
        num+=1
    print()       
1 
2,3
4,5,6
7,8,9,10
11,12,13,14,15