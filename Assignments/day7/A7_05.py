# A7_05. Write a program to print the even numbers from a given
# list using the lambda function.


user_input = input("Enter a list of numbers separated by spaces: ")
input_list = list(map(int, user_input.split()))  # Convert the input to a list of integers

even_numbers = list(filter(lambda x: x % 2 == 0, input_list))

print(f"The even numbers in the list are: {even_numbers}")
