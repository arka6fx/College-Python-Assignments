nst=2*5-1
nsp=0
for i in range(1,6):
     for j in range(1,nsp+1):
         print("  ", end="")
     for k in range(1,nst+1):
         print("* ", end="")     
     nst-=2
     nsp+=1
     print()
    
#Another method    
# for i in range(1,n+1):
#      print("  "*(nsp), end="")  
#      print("* "*(nst), end="")  
#      nst-=2
#      nsp+=1
#      print()    
