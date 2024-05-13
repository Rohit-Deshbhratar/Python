"""
Calculating discount on the basis of class attribute.
Discount will be different for different products. 
We can achieve this by assigning class attribute to instance of a class.
"""
class Item8:
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

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item8("Phone", 100, 5)
item2 = Item8("Laptop", 1000, 3)
item2.pay_rate = 0.7

item1.apply_discount()
item2.apply_discount()

print(item1.price)
print(item2.price)
