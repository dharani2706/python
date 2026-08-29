numbers = (10, 20, 30)
try:
    numbers[1] = 50
except TypeError:
    print("Error: Tuples cannot be modified")
#output:
    
Error: Tuples cannot be modified
