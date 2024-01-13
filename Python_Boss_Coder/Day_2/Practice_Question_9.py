import re

# Create a function to count the number of vowels in a given string.

test_string = "The quick brown fox jumps over the lazy dog"
vowels = "aeiouAEIOU"

#################################################################################
# Approach 1 --> loop

def count_vowels_loop(vow):
    count = 0
    for i in vow:
        if i in vowels:
            count = count + 1
    return count

result = count_vowels_loop(test_string)
print(f"Number of vowels in string are: {result}")
#################################################################################
# Approach  --> count()
def count_vowels(vow):
    result = sum(vow.count(i) for i in vowels)
    return result

print(f"Counting vowels using count() method: {count_vowels(test_string)}")
#################################################################################
# Approach  --> list comprehension

def count_vowels_lc(vow):
    return len([i for i in vow if i in vowels])

print(f"Counting vowels using list comprehension: {count_vowels_lc(test_string)}")
#################################################################################
# Approach  --> list comprehension
vowel = r'[aeiouAEIOU]'
def count_vowels_re(vow):
    return len(re.findall(vowel, vow))

print(f"Counting vowels using regular expression: {count_vowels_re(test_string)}")
#################################################################################
