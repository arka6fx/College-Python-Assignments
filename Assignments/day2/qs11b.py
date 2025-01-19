n=5
nst=2*n-1
nsp=0
for i in range(n):
     for j in range(nsp):
         print("  ", end="")
     for k in range(nst):
         print("* ", end="")     
     nst-=2
     nsp+=1
     print()
    
# Another method    
n=5
nst=2*n-1
nsp=0
for i in range(n):
     print("  "*(nsp), end="")  
     print("* "*(nst), end="")  
     nst-=2
     nsp+=1
     print()    

n=5

for i in range(n, 0, -1):
        for j in range(n-i):
            print("  ", end="")
        for k in range(2 * i - 1):
            print("* ", end="")
        print()       