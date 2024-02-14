# Write a program that calculates the factorial of a given number

num = int(input("Enter number: "))
#################################################################################
# Approach  -> 1. Recursion.
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(num))
#################################################################################
# Approach  -> 2. Ternary operator.
def factorial(n):
    return 1 if (n == 0 or n== 1) else n * factorial(n - 1)

print(factorial(num))
#################################################################################
# Approach  -> 3. WHILE loop.
def factorial(n):
    if (n == 0):
        return 1
    i = n
    fact = 1

    while(n / i != n):
        fact = fact * i
        i -= 1
    return fact

print(factorial(num))
#################################################################################
# Approach  -> 4. FOR loop.
def factorial(n):
    result = 1

    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(num))
#################################################################################
