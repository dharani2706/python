items = {
    "Book": 250,
    "Pen": 20,
    "Bag": 800,
    "Pencil": 10,
    "Bottle": 200
}
highest = max(items, key=items.get)
lowest = min(items, key=items.get)
print("Highest price item:", highest)
print("Price:", items[highest])
print("Lowest price item:", lowest)
print("Price:", items[lowest])
#output:
Highest price item: Bag
Price: 800
Lowest price item: Pencil
Price: 10
