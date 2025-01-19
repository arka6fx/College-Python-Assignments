
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))


if a <= b and a <= c:  
    if b <= c:
        print("Sorted order:", a, b, c)
    else:
        print("Sorted order:", a, c, b)
elif b <= a and b <= c:  
    if a <= c:
        print("Sorted order:", b, a, c)
    else:
        print("Sorted order:", b, c, a)
else:  
    if a <= b:
        print("Sorted order:", c, a, b)
    else:
        print("Sorted order:", c, b, a)
