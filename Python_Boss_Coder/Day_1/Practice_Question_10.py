# Implement a program that swaps the values of two variables.

num1 = 45
num2 = 23

print(f"Before swap: {num1, num2}")

num1, num2 = num2, num1
print(f"After swap: {num1, num2}", "\n")
#################################################################
x = 7
y = 3

print(f"Before swap: {x, y}")

temp = x
x = y
y = temp

print(f"After swap: {x, y}", "\n")
#################################################################

p = 78
q = 89

print(f"Before swap: {p, q}")

p = p + q
q = p - q
p = p - q

print(f"After swap: {p, q}", "\n")
#################################################################

j = 7
k = 9

print(f"Before swap: {j, k}")

j = j * k
k = j / k
j = j / k

print(f"After swap: {j, k}", "\n")
#################################################################
