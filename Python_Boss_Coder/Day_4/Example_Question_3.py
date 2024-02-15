# Implement a function that reverses a given string.

str = input("Enter string to reverse: ")

#################################################################################
# Approach 1 -> String slicing
def reverse_string_slicing(s):
    return s[::-1]

print(reverse_string_slicing(str))
#################################################################################
# Approach 2 -> FOR loop[]
def reverse_string_loop(s):
    string = ""

    for i in s:
        string = i + string
    return string

print(reverse_string_loop(str))
#################################################################################
# Approach 3 -> reversed() function
def reverse_string_rev(s):
    string = "".join(reversed(s))
    return string

print(reverse_string_rev(str))
#################################################################################
# Approach 4 -> list comprehension
def reverse_string_lc(s):
    string = [s[i] for i in range(len(s) - 1, -1, -1)]
    return "".join(string)

print(reverse_string_lc(str))
#################################################################################
