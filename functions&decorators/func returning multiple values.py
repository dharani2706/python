def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average
numbers = [10, 60, 30, 90, 120]
minimum, maximum, average = stats(numbers)
print("Numbers:", numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
#output:
Numbers: [10, 60, 30, 90, 120]
Minimum: 10
Maximum: 120
Average: 62.0
