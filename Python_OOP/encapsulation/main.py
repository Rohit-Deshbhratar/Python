from item import Item

item1 = Item("MyItem", 750)

item1.apply_increment(0.2)
print(f"After increment: {item1.price}")

item1.apply_discount()
print(f"After discount: {item1.price}")

# Setting an attribute
item1.name = "OtherItem"
print(f"After new name set: {item1.name}")

item1.__price = 900
print(f"After passing new value: {item1.__price}")
