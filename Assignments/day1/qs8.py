p=int(input("Enter principle amount: "))
r=int(input("Enter interest: "))
t=int(input("Enter duration: "))
s=(p*r*t)/100
t=p+s
print("Simple interest =",s)
print("Total amount =",t)
