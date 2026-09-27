def square(x):
    return x * x
def calculate(func, number):
    return func(number)
result = calculate(square, 5)
print("Result:", result)
#output:
Result: 25
