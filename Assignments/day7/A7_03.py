# A7_03. Write a program to find all the unique elements of a list by defining a function.


def find_unique_elements(input_list):

    unique_elements = []
    
    for element in input_list:
        if input_list.count(element) == 1:
            unique_elements.append(element)
    
    return unique_elements


  
user_input = input("Enter a list of elements separated by spaces: ")
input_list = user_input.split() 
   
unique_elements = find_unique_elements(input_list)
 
print(f"The unique elements in the list are: {unique_elements}")


