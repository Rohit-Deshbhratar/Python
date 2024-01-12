# Create a Python function to check if a given string is a palindrome

input_str = "nitin"

def palindrome(string):
    rev_str = string[::-1]
    if rev_str == string:
        print(f"{string} and {rev_str} are palindrome.")
    else:
        print(f"{string} and {rev_str} are not palindrome.")

palindrome(input_str)