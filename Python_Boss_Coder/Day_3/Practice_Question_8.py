# Create a loop that prints all prime numbers between 1 and 50

#################################################################################
# Approach -> 1. FOR loop.
def prime_number(begin, end):
    prime = []

    for i in range(begin, end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2) + 1):
                if i % j == 0:
                    break
            else:
                prime.append(i)
    return prime

start, stop = 2, 50
prime_list = prime_number(start, stop)

if len(prime_list) == 0:
    print("No prime number present.")
else:
    print("Prime numbers upto 50 are: ", prime_list)
#################################################################################
# Approach -> 1. Flag variable.
def prime_number(begin, end):
    prime = []
    flag = 0

    for i in range(begin, end):
        for j in range(2, i):
            if (i % j == 0):
                flag = 1
                break
            else:
                flag = 0
        if (flag == 0):
            prime.append(i)
    return prime

start, stop = 2, 50
prime_list = prime_number(start, stop)

if len(prime_list) == 0:
    print("No prime number present.")
else:
    print("Prime numbers upto 50 are: ", prime_list) 
#################################################################################
