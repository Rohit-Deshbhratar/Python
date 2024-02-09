# Implement a program that prints the multiplication table of a given number.

#################################################################################
# Approach  -> 1. Simple FOR loop
num = int(input("Please enter number: "))

for i in range(1, 11):
    print(i * num)
#################################################################################
# Approach  -> 2. WHILE loop
table = int(input("Enter number: "))
counter = 1

while counter != 11:
    print(table * counter)
    counter = counter + 1
#################################################################################
# Approach  -> 3. Function
def table(num):
    for i in range(1, 11):
        print("%d * %d = %d" % (num, i, num * i))

number = int(input("Enter number: "))
table(number)
#################################################################################
# Approach  -> 4. Recursion
def tables(num, i = 1):
    if (i == 11):
        return
    
    print(num, "*", i, "=", num * i)
    i+=1
    tables(num, i)

numbers = int(input("Enter number: "))
tables(numbers)
#################################################################################
