#  Write a Python function to check if a given string is a palindrome

str = input("Enter string: ")

def palindrome(s):
    rev = s[::-1]
    if s == rev:
        print("String is palindrome.")
    else:
        print("String is not palindrome.")

palindrome(str)