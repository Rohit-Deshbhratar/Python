"""
Set default data type in __init__() method.
"""
class Item4:
    def __init__(self, name: str, price: float, quantity=0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

# Pass only first 2 parameter in either of these methods.
item1 = Item4("Phone", 100, 5)
item2 = Item4("Laptop", 1000, 3)

print("After initialization.")
print(f"Item name = {item1.name}")
print(f"Price = {item1.price}")
print(f"Quantity = {item1.quantity}")
print(f"Item name = {item2.name}")
print(f"Price = {item2.price}")
print(f"Quantity = {item1.quantity}")

print("Total Price = ",item1.calculate_total_price())
print("Total Price = ",item2.calculate_total_price())
