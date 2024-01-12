# Given a list of numbers, find the sum and average.

numbers = [10, 5, 8, 7, 23, 56, 99] # 208
length = len(numbers)
add = 0
for i in numbers:
    add = add + i

average = add / length

print(f"Addition is: {add}, average is: {average}")
