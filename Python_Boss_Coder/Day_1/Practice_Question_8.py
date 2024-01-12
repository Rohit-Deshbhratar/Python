# Given a list of integers, find the sum of all positive numbers

numbers = [2, 7, 9, 6, -1, 45, 23, 78, -56]
add= 0

for i in numbers:
    if i < 0:
        continue
    else:
        add = add + i

print(f"Addition is {add}: ")