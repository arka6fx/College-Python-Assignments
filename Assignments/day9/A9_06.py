# A9_06.  Write a program to read the age of a person and raise exceptions if age is negative.


try:
    age = int(input("Enter the age of the person: "))
    
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    print(f"The age of the person is: {age}")

except ValueError as e:
    print(f"Error: {e}")
