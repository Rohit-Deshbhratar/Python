from math import pi
# Write a function to calculate the area of a circle given its radius

def circle_area(r):
    return pi * r * r

radius = float(input("Enter radius of a circle: "))

print("Area of circle is: ", format(circle_area(radius), ".2f"))