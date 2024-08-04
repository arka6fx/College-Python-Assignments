nst=2*5-1
nsp=0
n=5
for i in range(1,n+1):
    for j in range(1,nsp+1):
         print("  ", end="")
    for k in range(1,nst+1):
         print("* ", end="")     
    nst-=2
    nsp+=1
    print()
    

