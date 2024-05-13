from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0) -> None:
        # Call super function to have access to attributes/methods.
        super().__init__(name, price, quantity)

        # Run validations to the received arguments.
        assert broken_phone >= 0, f"Broken Phone {broken_phone} should be greater than or equal to zero."

        # Assign to self object
        self.broken_phone = broken_phone

phone1 = Phone("Oppo", 5000, 7)
phone2 = Phone("vivo", 9000, 8)

print(phone1.calculate_total_price())
print(Phone.all)


