import csv
"""
The data on which we were operating till now is stored in a .csv file.
We are also using a decorator "@classmethod", used to declare method belonging to the class.
"""
class Item10:
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
        Item10.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item10(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
            )

    def __repr__(self) -> str:
        return f"Item10('{self.name}', '{self.price}', '{self.quantity}')"

Item10.instantiate_from_csv()
print(Item10.all)