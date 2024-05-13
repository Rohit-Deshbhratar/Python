"""
Passing values as a parameter and assigning these values to class attributes.
quantity=0 in __init__() method is default value. If don't pass value in quantity it will take zero as a value in __init__() method.
Try to pass only two parameter in any of the two method the total price will be zero in output.
"""
class Item3:
    def __init__(self, name, price, quantity=0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

# Pass only first 2 parameter in either of these methods.
item1 = Item3("Phone", 100, 5)
item2 = Item3("Laptop", 1000, 3)

print("After initialization.")
print(f"Item name = {item1.name}")
print(f"Price = {item1.price}")
print(f"Quantity = {item1.quantity}")
print(f"Item name = {item2.name}")
print(f"Price = {item2.price}")
print(f"Quantity = {item1.quantity}")

print("Total Price = ",item1.calculate_total_price())
print("Total Price = ",item2.calculate_total_price())
