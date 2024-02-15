# Given a list of numbers, create a function to find the sum of all positive numbers

num_list = [12, 15, 5, -3, 8, -7, 74, -9]
num = 0

for i in num_list:
    if i < 0:
        continue
    else:
        num = num + i

print(num)
