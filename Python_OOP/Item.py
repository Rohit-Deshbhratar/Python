"""
Basics of  'CLASS' in python.
item1 is an object/instance of class Item.
item1.name is an attribute
item1.price is an attribute
item1.quantity is an attribute

##################### OUTPUT ##################### 
<class '__main__.Item'>
<class 'str'>
<class 'int'>
<class 'int'>
<class 'float'>
"""

class Item:
    pass

item1 = Item() # 
item1.name = "Phone" 
item1.price = 100
item1.quantity = 5
item1.commission = 0.05

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
print(type(item1.commission))
####################################################################################
# calculating total price
print("Total Price = ",item1.calculate_total_price(item1.price, item1.quantity))

# calculating total commission
print("Commission = ",item1.calculate_total_commission(item1.price, item1.quantity, item1.commission))
