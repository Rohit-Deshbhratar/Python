# Given a list of integers, find all the even numbers and store them in a new list.

num_list = [1, 2, 5, 4, 7, 9, 12, 18, 19, 22, 27, 28, 30]
even_num = []
#################################################################################
# Approach  -> 1. Simple loop.
for i in num_list:
    if(i % 2 == 0):
        even_num.append(i)
    else:
        continue

print(even_num)
#################################################################################
# Approach  -> 2. List comprehension.
even_num = [i for i in num_list if i % 2 == 0]
print(f"Even numbers: {even_num}")
#################################################################################
# Approach  -> 3. While loop.
i = 0
while(i < len(num_list)):
    if num_list[i] % 2 == 0:
        print(num_list[i], end=" ")
    i+=1
#################################################################################
# Approach  -> 4. Lambda expression.
even_num = list(filter(lambda x: (x%2==0), num_list))
print("\n",even_num)
#################################################################################
# Approach  -> 5. Enumerate Function.
for a,i in enumerate(num_list):
    if (i % 2 == 0):
        print(i, end=" ")
#################################################################################
# Approach  -> 6. Recursion.
def even_number(lst, n=0):
    if n == len(lst):
        exit()
    if lst[n] % 2 == 0:
        print(lst[n], end=" ")
    
    even_number(lst, n+1)

even_number(num_list)
#################################################################################
