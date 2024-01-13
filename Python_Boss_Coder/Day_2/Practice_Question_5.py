from functools import reduce

# Given a list of names, concatenate them into a single string separated by spaces.

names = ['ricky', 'sanu', 'viraj', 'riyan', 'anvika']
name_join = " ".join(names)

print(name_join)

####################################################################################
for i in names:
    print(i, end=" ")
print("\n")
####################################################################################
names_map = map(str.strip, names)
print(" ".join(names_map))
####################################################################################
names_lambda = reduce(lambda x,y: x + ' ' + y, names)

print(names_lambda)
####################################################################################
