# Write a program to convert given number of days into years, weeks and days.

inputs = int(input("Enter number of days: "))

weeks = int((inputs % 365) / 7)
days = int((inputs % 365) % 7)
years = int(inputs / 365)

print(f"Given days {inputs}, years={years}, weeks={weeks}, days={days}")