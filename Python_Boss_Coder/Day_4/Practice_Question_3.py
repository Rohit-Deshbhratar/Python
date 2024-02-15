# Implement a function that returns the factorial of a given number using recursion

num = int(input("Enter number: "))

def factorial(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * factorial(f - 1)

print(factorial(num))