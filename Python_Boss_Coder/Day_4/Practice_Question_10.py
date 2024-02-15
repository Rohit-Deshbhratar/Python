# Create a function that takes a number as input and prints its multiplication table

number = int(input("Enter number: "))

def table(n):
    for i in range(1, 11, 1):
        print(f"{n} * {i} = ", i * n)

table(number)