# Create a list of fruits and access elements using indexing.

fruits = ['apple', 'orange', 'mango', 'pine apple', 'grapes']

print(f"Fruit at index[0]: {fruits[0]}")
print(f"Fruit at index[1]: {fruits[1]}")
print(f"Fruit at index[2]: {fruits[2]}")
print(f"Fruit at index[3]: {fruits[3]}")
print(f"Fruit at index[4]: {fruits[4]}")

print("Using for loop")
for i in fruits:
    print(f"Fruit at index[{fruits.index(i)}]: {i}")
    
