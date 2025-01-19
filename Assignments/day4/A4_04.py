#A4_04) Write a program to count the occurrences of a word in a given sentence.

sentence = input("Write a sentence: ")
word = input("Enter the word you want to find: ")
word=word.lower()
sentence = sentence.lower()
count = sentence.count(word)

print(f"The word '{word}' appears {count} times in the sentence.")
