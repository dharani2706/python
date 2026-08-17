num = int(input("Enter a number: "))
temp = num
sum = 0
count = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit
    count = count + 1
    temp = temp // 10
average = sum / count
print("Sum =", sum)
print("Average =", average)
output:
    Enter a number: 1467
Sum = 18
Average = 4.5
