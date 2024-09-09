# A6_03. Write a program to create a dictionary by combining two lists ‘ name’ 
# for employee name and ‘salary’ for employee salary. 
# Use the list ‘name’ as the key and ‘salary’ 
# as the value of dictionary elements.


names_input = input("Enter employee names separated by commas: ")
names = [name.strip() for name in names_input.split(',')]


salaries_input = input("Enter corresponding salaries separated by commas: ")
salaries = [salary.strip() for salary in salaries_input.split(',')]

employee_dict = {}

if len(names) == len(salaries):
    
    for i in range(len(names)):
        if salaries[i].isdigit():
            salary = int(salaries[i])
            employee_dict[names[i]] = salary
        else:
            print(f"Error: '{salaries[i]}' is not a valid number. Skipping this entry.")
else:
    print("Error: The number of names and salaries must be the same.")


print("Employee Dictionary:")
print(employee_dict)


