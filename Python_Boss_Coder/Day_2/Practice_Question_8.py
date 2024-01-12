# Implement a program that converts a given number of minutes into hours and minutes.

inputs = int(input("Enter minutes: "))

hours = int(inputs / 60)
minutes = int(inputs % 60)

print(f"You entered {inputs}, Hours: {hours} Minutes: {minutes}.")
