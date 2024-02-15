# Write a function that takes two lists and returns their intersection (common elements)

list_A = [1, 2, 3, 4]
list_B = [1, 3, 5, 6]
#################################################################################
# Approach -> 1. Sets.
def intersection(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(list(a_set & b_set))
    else:
        print("No common elements.")

intersection(list_A, list_B)
#################################################################################
# Approach -> 2. Sets intersection property.
def intersect(a, b):
    a_set = set(a)
    b_set = set(b)

    if (len(a_set.intersection(b_set))> 0):
        return list(a_set.intersection(b_set))
    else:
        print("No common element")

print(intersect(list_A, list_B))
#################################################################################
# Approach -> 3. FOR loop.
def insersect_loop(a, b):
    res = [i for i in a if i in b]
    return res

print(insersect_loop(list_A, list_B))
#################################################################################
# Approach -> 4. set() method.
def intersect_set(a, b):
    return list(set(a).intersection(b))

print(intersect_set(list_A, list_B))
#################################################################################