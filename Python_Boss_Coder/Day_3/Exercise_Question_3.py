# Implement a program that finds the largest number in a list.

max_num_list = [10, 25, 31, 45, 41, 17, 29]

#################################################################################
# Approach 1 -> sort()

list_length = len(max_num_list) - 1
max_num_list.sort()
print(max_num_list[-1])
#################################################################################
# Approach 2 -> max()
print(max(max_num_list))
#################################################################################
# Approach 3 -> function
def largest_number(numbers):
    largest_number = numbers[0]

    for num in numbers:
        if num > largest_number:
            largest_number = num

    return largest_number

largest_number = largest_number(max_num_list)
print(f"The largest number in the list is: {largest_number}")
#################################################################################
# Approach 4 -> lambda function
print(max(max_num_list, key=lambda value: int(value)))
#################################################################################
