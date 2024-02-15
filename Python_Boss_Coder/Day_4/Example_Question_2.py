# Create a function to check if a number is prime.

#################################################################################
prime = int(input("Enter number: "))

if prime > 1:
    for i in range(2, int(prime / 2) + 1):
        if (prime % i) == 0:
            print("Not a prime number.")
            break
    else:
        print("It is a prime number.")
else:
    print("Not a prime number.")