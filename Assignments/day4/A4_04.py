#A4_04) Write a program to count the occurrences of a word in a given sentence.

sentence = input("Write a sentence: ")
word = input("Enter the word you want to find: ")

sentence = sentence.lower()
word = word.lower()

words = sentence.split()

count = words.count(word)

print(f"The word '{word}' appears {count} times in the sentence.")
