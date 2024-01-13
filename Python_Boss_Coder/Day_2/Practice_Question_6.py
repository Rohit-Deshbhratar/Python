import re
import string
# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

test_string = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
####################################################################################
# Approach 1
def is_panagram_naive(pan_str):
    for i in alphabet:
        if i not in pan_str.lower():
            return False
    return True

if(is_panagram_naive(test_string) == True):
    print("The string is panagram.")
else:
    print("The string is not panagram.")
####################################################################################
# Approach 2
    
char_set = set(string.ascii_lowercase)

def is_panagram_set(pan_str):
    return set(pan_str.lower()) >= char_set

if(is_panagram_set(test_string) == True):
    print("The string is panagram.")
else:
    print("The string is not panagram.")
####################################################################################
# Approach 3

def is_panagram_alt_set(pan_str):
    return not set(char_set) - set(pan_str)

if(is_panagram_alt_set(test_string) == True):
    print("The string is panagram.")
else:
    print("The string is not panagram.")
####################################################################################
# Approach 4

def is_panagram_re(pan_str):
    lower_string = re.sub('[^a-z]', '', pan_str.lower())
    alpha_size = len(set(lower_string))
    return alpha_size == 26

if(is_panagram_alt_set(test_string) == True):
    print("The string is panagram.")
else:
    print("The string is not panagram.")
####################################################################################
