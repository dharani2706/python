def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
n=int(input("enter a number"))
print("Recursive factorial:", factorial(n))
print("Iterative factorial:", factorial_iterative(n))
print("Factorial of 0:", factorial(0))
print("Negative input:", factorial(-2))
#output:
enter a number7
Recursive factorial: 5040
Iterative factorial: 5040
Factorial of 0: 1
Negative input: Factorial is not defined for negative numbers
