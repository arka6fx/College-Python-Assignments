# A7_04. Write a program to find all the numbers divisible by 5 and 7 between 
# the given range using the lambda function.


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

divisible_by_5_and_7 = list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(start, end + 1)))


print(f"Numbers divisible by 5 and 7 between {start} and {end}: {divisible_by_5_and_7}")

