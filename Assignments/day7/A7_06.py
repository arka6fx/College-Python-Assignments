# A7_06. Write a program to find the maximum value from a list using the lambda function.




user_input = input("Enter a list of numbers separated by spaces: ")
input_list = list(map(int, user_input.split()))

max_value = input_list[0]

for num in input_list[1:]: 
    max_value = (lambda x, y: x if x > y else y)(max_value, num)

print(f"The maximum value in the list is: {max_value}")
