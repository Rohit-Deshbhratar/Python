"""
Creating and accessing class attribute.
Till now we have learned about instance variables.
A class attribute is an attribute that belongs to the class but you can access this attribute at instance level.
"""
class Item6:
    pay_rate = 0.8 # The pay rate after 20% discount

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
item1 = Item6("Phone", 100, 5)
item2 = Item6("Laptop", 1000, 3)

# Accessing by class name
print(Item6.pay_rate) 

# Accessing by instance of a class
print(item1.pay_rate)
print(item2.pay_rate)

# How to find class level attributes and instance level attributes
print(Item6.__dict__) # Class level attributes
print(item1.__dict__) # Instance level attributes
