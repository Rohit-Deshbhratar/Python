"""
Using assertion to validate data.
"""
class Item4:
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received arguments.
        assert price > 0, f"Price {price} should be greater than zero."
        assert quantity > 0, f"Quantity {quantity} should be greater than or equal to zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

# Pass only first 2 parameter in either of these methods.
item1 = Item4("Phone", 100, 5)
item2 = Item4("Laptop", 1000, 3)

print("Total Price = ",item1.calculate_total_price())
print("Total Price = ",item2.calculate_total_price())
