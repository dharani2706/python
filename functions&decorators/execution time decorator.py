import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper
def calculate_sum():
    total = 0
    for i in range(1, 1000001):
        total = total + i
    return total
result = calculate_sum()
print("Sum:", result)
#output:
Sum: 500000500000
