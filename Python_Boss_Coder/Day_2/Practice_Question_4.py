# Create a function to reverse a given string.

original_string = "rohit"

########################################################################
def reverse_string_slice(string):
    return string[::-1]

print(f"Reverse using slice: {reverse_string_slice(original_string)}")
########################################################################
# LC = list comprehension
def reverse_string_LC(string):
    rev_string = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join(rev_string)

print(f"Reverse using list comprehension: {reverse_string_LC(original_string)}")
########################################################################
def reverse_string(string):
    rev_str = "".join(reversed(string))
    return rev_str

print(f"Reverse using reversed(): {reverse_string(original_string)}")
########################################################################
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

print(f"Reverse using recursion: {reverse(original_string)}")
########################################################################
def reverse_string_loop(string):
    str = ""
    for i in string:
        str = i + str
    return str

print(f"Reverse using for loop: {reverse_string_loop(original_string)}")
########################################################################
