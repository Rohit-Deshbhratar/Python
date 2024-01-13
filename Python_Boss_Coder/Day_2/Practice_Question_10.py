# Write a program to check if a number is prime.

prime = int(input("Enter integer number to check it is prime number or not: "))

if prime > 1:
    for i in range(2, int(prime / 2) + 1):
        if (prime % i) == 0:
            print(f"{prime} Not prime number.")
            break
    else:
        print(f"{prime} Is a prime number.")
else:
    print(f"{prime} Is not a prime number.")
