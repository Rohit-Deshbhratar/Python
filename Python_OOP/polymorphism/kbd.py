from item import Item

class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Call super function to have access to attributes/methods.
        super().__init__(name, price, quantity)
