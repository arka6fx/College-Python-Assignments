a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))
i=1
if a<b:
    min = a
else:
    min = b
    
while i<=min:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print('HCF = ',hcf)    
        