items = {
    "Pen": 20,
    "Notebook": 50,
    "Pencil": 10,
    "Bag": 500,
    "Eraser": 5
}
sorted_items = sorted(items.items(), key=lambda item: item[1])
print("Items from cheapest to most expensive:")
for item, price in sorted_items:
    print(item, ":", price)
#output:
Items from cheapest to most expensive:
Eraser : 5
Pencil : 10
Pen : 20
Notebook : 50
Bag : 500
