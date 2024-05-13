from phone import Phone

item1 = Phone("iPhone", 1000, 3)

item1.apply_increment(0.2)
print(item1.price)

item1.send_emails()
