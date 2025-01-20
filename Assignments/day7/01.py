#function
'''
int add(int a, int b){
c= a+b
return c
}'''
#Function definition
def add(a,b):
    c=a+b
    return c

#function call
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r=add(x,y)
print(r)