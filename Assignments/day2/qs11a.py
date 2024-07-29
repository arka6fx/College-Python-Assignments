n = 5  # Number of rows

num = 1
for i in range(1, n+1):
    for j in range(i):
        if j==i-1:
            print(num, end=" ")
        else :
            print(num, end=",")     
        num += 1
    print()
