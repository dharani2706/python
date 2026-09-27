square = lambda x: x * x
even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b
print("Square:", square(5))
print("Is 8 even?", even(8))
print("Larger number:", larger(10, 7))
#output:
Square: 25
Is 8 even? True
Larger number: 10
