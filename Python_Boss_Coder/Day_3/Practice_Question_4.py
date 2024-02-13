#  Create a program that generates the Fibonacci sequence up to a given number of terms

#################################################################################
# Approach  -> 1. Simple FOR loop.
# num = int(input("Enter number: "))
# a, b = 0, 1

# print("Fibbonacci series: ",a,", ", b, end=" , ")

# for i in range(2, num):
#     c = a + b
#     a = b
#     b = c
#     print(c, ",",end=" ")
#################################################################################
# Approach  -> 2. Recursion.
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# number = int(input("Enter number: "))
# for i in range(0, number):
#     print(fibo(i), end=" ")
#################################################################################
# Approach  -> 3. WHILE loop.
n = int(input("Enter number: "))
a, b = 0, 1
sum = a + b
counter = 1

print("Fibbonacci series: ", end=" ")

while(counter <= n):
    counter += 1
    print(a, end=" ")
    a = b
    b = sum
    sum = a + b
#################################################################################