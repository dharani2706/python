my_tuple = (10, 20, [30, 40, 50])
print("Before modification:", my_tuple)
my_tuple[2].append(60)
print("After modification:", my_tuple)
#output:
Before modification: (10, 20, [30, 40, 50])
After modification: (10, 20, [30, 40, 50, 60])
