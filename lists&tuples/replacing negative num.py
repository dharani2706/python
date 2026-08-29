numbers=[10,20,-2,40,-5,-7,50]
new_list = [number if number >= 0 else 0 for number in numbers]
print("Original list:", numbers)
print("New list:", new_list)
#output:
Original list: [10, 20, -2, 40, -5, -7, 50]
New list: [10, 20, 0, 40, 0, 0, 50]
