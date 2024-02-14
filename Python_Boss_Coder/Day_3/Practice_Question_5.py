import re
# Given a list of names, print all names starting with the letter 'A'.

name_list = ['rohit', 'akash', 'Anvika', 'arman']
look_for = 'A'
#################################################################################
# Approach  -> 1. Simple loop and 'startswith()' function.
for i in name_list:
    if i.startswith('A') or i.startswith('a'):
        print(i, end=", ")
#################################################################################
# Approach  -> 2. List comprehension and 'lower()' function.
result = [i for i in name_list if i[0].lower() == look_for.lower()]
print("\nName starts with 'A': ", result)
#################################################################################
# Approach  -> 3. List comprehension, 'startswith()' and 'lower()' function.
result = [i for i in name_list if i.lower().startswith(look_for.lower())]
print("Name starts with 'A': ", result)
#################################################################################
# Approach  -> 4. 'find()' and 'lower()' function.
result = []
for i in name_list:
    if(i.find(look_for) == 0 or i.find(look_for.lower()) == 0):
        result.append(i)

print("Name starts with 'A': ", result)
#################################################################################
# Approach  -> 5. 'filter()' and 'lambda' function.
result = list(filter(lambda x: x[0].lower() == look_for.lower(), name_list))
print("Name starts with 'A': ", result)
#################################################################################
# Approach  -> 6. Regular expression.
look_for_lower = look_for.lower()
result = [i for i in name_list if re.match("^{}".format(look_for_lower), i.lower())]
print("Name starts with '{}': {}".format(look_for_lower, result))
#################################################################################
