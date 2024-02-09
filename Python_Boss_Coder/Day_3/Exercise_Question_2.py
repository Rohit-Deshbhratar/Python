# Create a loop that prints the first 10 even numbers.

#################################################################################
# Approach 1 -> For Loop
num = int(input("Enter number to print it's first 10 even numbers: "))
count = 0

for even in range(1, num + 1):
    if (even%2 == 0):
        print(even, end=" ")
        count+=1
        if(count == 10):
            break
#################################################################################
# Approach 2 -> While Loop
nums = int(input("\nEnter a Number: "))
counter = 0
e = 1

while (e <= nums) and (counter < 10):
    if (e % 2 == 0):
        print(e, end=" ")
        counter+=1
    e+=1
#################################################################################
# Approach 3 -> Recursion

begin = int(input("Enter start number: "))
end = int(input("Enter stop number: "))
ct = int(input("How many even numbers you want to print?: "))

def print_even_numbers(start, stop, count):
    if count == 0:
        return
    if start%2==0:
        print(start, end=" ")
        print_even_numbers(start + 1, stop, count - 1)
    else:
        print_even_numbers(start + 1, stop, count)

print_even_numbers(begin, end, ct)

