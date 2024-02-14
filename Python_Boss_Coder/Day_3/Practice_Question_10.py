# Calculate the sum of digits of a given number
number = int(input("Enter number: "))

#################################################################################
# Approach -> 1. WHILE loop.

def sum_of_number(x):
    sum = 0

    while (x != 0):
        sum = sum + int(x % 10)
        x = int(x / 10)
    
    return sum

print(sum_of_number(number))
#################################################################################
# Approach -> 2. Recursion.
def sum(x):
    return 0 if x == 0 else int(x % 10) + sum(int(x / 10))

print(sum(number))
#################################################################################
