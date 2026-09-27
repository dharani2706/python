def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    price_with_tax = price + tax
    final_price = price_with_tax - discount
    return final_price
# (a) Only price
print("Only Price:", calculate_price(1000))
# (b) Price and custom tax rate
print("Custom Tax Rate:", calculate_price(1000, 20))
# (c) All three arguments
print("All Arguments:", calculate_price(1000, 20, 50))
#output:
Only Price: 1180.0
Custom Tax Rate: 1200.0
All Arguments: 1150.0
