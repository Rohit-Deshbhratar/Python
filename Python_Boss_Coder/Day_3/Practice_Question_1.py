import calendar
# Create a program that takes a year as input and checks if it is a leap year or not.

#################################################################################
# Approach  -> 1. Simple Conditions.
year = int(input("Enter year: "))
if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#################################################################################
# Approach  -> 2. In-built function.
yrs = int(input("Enter year: "))

if calendar.isleap(yrs):
    print("Leap Year.")
else:
    print("Not a leap year.")
#################################################################################
# Approach  -> 3. Function.
def checkYear(y):
    if((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")

year = int(input("Enter year: "))
checkYear(year)
#################################################################################
