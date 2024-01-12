# Given a list of numbers, find the maximum and minimum values.

numbers = [2, 5, 8, 10, 7, 23]
print(f"Minimum number: {min(numbers)}")
print(f"Maximum number: {max(numbers)}")

######################################################################################

length = len(numbers)
numbers.sort()
print(f"Min number = {numbers[0]}, Max number is {numbers[length - 1]}")

######################################################################################

max = min = numbers[0]
for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i
print(f"Max={max}, min={min}")
        
