#  Calculate the area of a triangle given its base and height using a function

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

def triangle_area(b, h):
    return 0.5 * b * h

print(f"Area of triangle is: {triangle_area(base, height)}")
