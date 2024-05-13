import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received arguments.
        assert price > 0, f"Price {price} should be greater than zero."
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to zero."

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property decorator = Raed-Only attribute
    def name(self):
        return self.__name
    
    @price.setter
    def price(self, value):
        self.__price = value
    
    @name.setter
    # setter will allow to change name of item
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long!")
        else:
            self.__name = value
    
    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        # count floats that are point zero i.e. 5.0, 9.0 etc
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"

print(Item.is_integer(7))
