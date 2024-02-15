# Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly

def even_odd(n):
    if (n % 2 == 0):
        print("Even")
    else:
        print("Odd")

num = int(input("Enter number: "))

even_odd(num)