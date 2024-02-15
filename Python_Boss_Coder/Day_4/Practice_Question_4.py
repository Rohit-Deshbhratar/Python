from math import exp
# Create a function to find the square of each element in a given list

num_list = [2, 5, 8, 9, 12, 25, 30]

def square(nl):
    for i in num_list:
        print(i * i, end=" ")

print("Original list: ", num_list)
square(num_list)