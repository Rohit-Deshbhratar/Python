"""
Creating a method in a class which accepts parameter and returning value using return keyword
"""
class Item1:
    def calculate_total_price(self, x, y):
        return x * y

item1 = Item1()
item1.name = "Phone" 
item1.price = 100
item1.quantity = 5

print("Total Price = ",item1.calculate_total_price(item1.price, item1.quantity))