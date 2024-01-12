# Implement a program that checks if a given string is a palindrome

original_string = input("Enter string: ")
reverse_string = original_string[::-1]

print(f"Original string: {original_string}, Reverse string: {reverse_string}")

if original_string.isalpha():
    if original_string == reverse_string:
        print(f"String is pallindrome")
    else: 
        print(f"String is not pallindrome")
else:
    print("Oh NO !!! You entered text with numbers :(\nPlease Enter only alphabets.")
