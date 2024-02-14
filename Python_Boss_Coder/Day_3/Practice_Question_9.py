import re

# Given a list of words, count the number of words with more than five characters

test_string = "Rohit ricky arman lata subodh sanu"
word = test_string.split()
count = 0
#################################################################################
# Approach -> 1. Simple FOR loop.
def count_word_char(str):
    for i in str:
        if len(i) == 5:
            print(i, end=", ")
        else:
            continue

count_word_char(word)
#################################################################################
# Approach -> 2. Regular expression.
words = re.findall(r"\w+",test_string)
print()
count_word_char(words)
#################################################################################
# Approach -> 3. Apending in list.
result = re.split(r"\W+", test_string)
final_words = []

for i in result:
    if len(i) == 5:
        final_words.append(i)
    else:
        continue
print(final_words)  
#################################################################################
