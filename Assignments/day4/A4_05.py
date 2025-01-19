#A4_05) ***Write a program to get all substring of a given string.

s = input('Enter a string: ')
print(f"All substrings of '{s}'")

for start in range(len(s)):
    for end in range(start + 1, len(s) + 1):
        print(s[start:end])
