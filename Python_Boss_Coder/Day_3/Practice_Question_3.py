from math import sqrt
#   Write a Python program to check if a given number is a prime number.

#################################################################################
# Approach  -> 1. Flag Variable.
num = int(input("Enter number: "))
flag = 0

if(num > 1):
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i == 0):
            flag = 1
            break
    if (flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
#################################################################################
# Approach  -> 2. Recursion.
def prime(n, i):
    if i == 1:
        return True
    if n % i == 0:
        return False
    if prime(n, i - 1) == False:
        return False
    return True

number = int(input("Enter number: "))
itr = int(sqrt(number) + 1)

print(prime(number, itr))
