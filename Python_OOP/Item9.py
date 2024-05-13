"""
Use of "all".
Now we have 5 items and they all have different pay_rate.
So we are going to assign all instances to "all" using list.
And printing appended values in a list.
"""
class Item9:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received arguments.
        assert price > 0, f"Price {price} should be greater than zero."
        assert quantity > 0, f"Quantity {quantity} should be greater than or equal to zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item9.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item9('{self.name}', '{self.price}', '{self.quantity}')"

item1 = Item9("Phone", 100, 5)
item2 = Item9("Laptop", 1000, 3)
item3 = Item9("Cable", 10, 5)
item4 = Item9("Mouse", 50, 5)
item5 = Item9("Keyboard", 75, 5)

# Print instances of class
print(Item9.all)

# Print name of instances
for instance in Item9.all:
    print(instance.name)

