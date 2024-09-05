#A5_07. Write a program to accept a sequence of comma-separated numbers 
# from the user and generate a tuple with those numbers.

user_input = input("Enter a sequence of comma-separated numbers: ")

number_strings = user_input.split(',')

numbers = tuple(int(num.strip()) for num in number_strings)

print("The tuple is:", numbers)
