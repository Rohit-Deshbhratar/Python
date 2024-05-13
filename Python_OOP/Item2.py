"""
Creating a constructor in a class which accepts parameter i.e. assigning attributes dynamically.
NOTE: comment first print stament in __init__() method and uncomment last 2 lines and vice versa.
"""
class Item2:
    def __init__(self, name) -> None:
        print(f"An instance created for {name}")
        self.name = name

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item2("Phone")
item1.price = 100
item1.quantity = 5

item2 = Item2("Laptop")
item2.price = 1000
item2.quantity = 3

print("Total Price = ",item1.calculate_total_price(item1.price, item1.quantity))

# print(item1.name)
# print(item2.name)
