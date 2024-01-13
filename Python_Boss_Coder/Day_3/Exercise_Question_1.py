# Write a program that checks if a given number is positive, negative, or zero.

number = int(input("Enter integer number: "))

if number == 0:
    print(f"You entered {number}")
elif number < 0:
    print(f"You entered negative number: {number}")
elif number > 0:
    print(f"You entered positive number: {number}")



