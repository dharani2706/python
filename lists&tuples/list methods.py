numbers = [30, 10, 20]
print("Original list:", numbers)
numbers.append(40)
print("After append:", numbers)
numbers.insert(1, 15)
print("After insert:", numbers)
numbers.extend([50, 60])
print("After extend:", numbers)
numbers.remove(15)
print("After remove:", numbers)
numbers.pop()
print("After pop:", numbers)
numbers.sort()
print("After sort:", numbers)
numbers.reverse()
print("After reverse:", numbers)
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))
#output:
Original list: [30, 10, 20]
After append: [30, 10, 20, 40]
After insert: [30, 15, 10, 20, 40]
After extend: [30, 15, 10, 20, 40, 50, 60]
After remove: [30, 10, 20, 40, 50, 60]
After pop: [30, 10, 20, 40, 50]
After sort: [10, 20, 30, 40, 50]
After reverse: [50, 40, 30, 20, 10]
Count of 20: 1
Index of 30: 2
