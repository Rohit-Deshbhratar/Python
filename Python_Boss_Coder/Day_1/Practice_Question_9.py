# Create a program that takes a sentence as input and counts the number of words in it
import re
import string

# sentence = input("Enter a sentence: ")
sentence = "rohit viraj * - $"
word_count = sentence.split()

print(f"Sentence has {len(word_count)} words.")
######################################################################################
# Does not read special characters
result = len(re.findall(r'\w+', sentence))
print(f"Sentence has {result} words.")
######################################################################################
# Does not read special characters
count = sum([i.strip(string.punctuation).isalpha() for i in sentence.split()])
print(f"Sentence has {count} words.")
######################################################################################

count = sentence.count(" ") + 1
print(f"Sentence has {count} words.")
######################################################################################
