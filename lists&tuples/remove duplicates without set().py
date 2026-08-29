numbers = [10, 20, 10, 30, 20, 40, 30]
s = []
for number in numbers:
    if number not in s:
        s.append(number)
print("Original list:", numbers)
print("List without duplicates:", s)
#output:
Original list: [10, 20, 10, 30, 20, 40, 30]
List without duplicates: [10, 20, 30, 40]

