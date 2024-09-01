#A4_04) Write a program to count the occurrences of a word in a given sentence.

sentence = input("Write a sentence: ")
word = input("Enter the word you want to find: ")

sentence = sentence.lower()
count = sentence.count(word.lower())

print(f"The word '{word}' appears {count} times in the sentence.")
