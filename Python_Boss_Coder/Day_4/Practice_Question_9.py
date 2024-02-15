# Implement a function to check if a given year is a leap year or not

def leap_year(y):
    if ((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):
        print("It is a leap year")
    else:
        print("It is not a leap year.")

year = int(input("Enter year: "))
leap_year(year)