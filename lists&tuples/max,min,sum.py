numbers = [10, 25, 5, 40, 15]
max = numbers[0]
min = numbers[0]
total = 0
for number in numbers:
    if number > max:
        max = number
    if number < min:
        min = number
    total = total + number
print("Max:", max)
print("Min:", min)
print("Sum:", total)
#output:
Max: 40
Min: 5
Sum: 95
