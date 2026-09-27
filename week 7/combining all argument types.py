def order_summary(customer, *items, discount=0, **extra):
    print("ORDER SUMMARY")
    print("Customer:", customer)
    print("Ordered Items:")
    for item in items:
         print("-", item)
         print("Discount:", discount, "%")
         print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").capitalize() + ":", value)
        print("")
order_summary(
    "Priya",
    "Laptop",
    "Wireless Mouse",
    "Keyboard",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)
#output:
ORDER SUMMARY
Customer: Priya
Ordered Items:
- Laptop
Discount: 10 %
Extra Information:
- Wireless Mouse
Discount: 10 %
Extra Information:
- Keyboard
Discount: 10 %
Extra Information:
Delivery address: Hyderabad

Gift wrap: True
