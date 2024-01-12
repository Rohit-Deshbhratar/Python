# Create a program that takes a temperature in Celsius and converts it to Kelvin.

celcius = float(input("Enter temperature in celcius: "))

def celcius_to_kelvin(c):
    kelvin = c + 273.15
    return kelvin

print(f"{celcius} Celcius is {celcius_to_kelvin(celcius)} kelvin.")
