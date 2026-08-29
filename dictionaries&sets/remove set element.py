my_set = {10, 20, 30, 40}
my_set.remove(20)
print("After remove():", my_set)
my_set.discard(30)
print("After discard():", my_set)
my_set.discard(80)
print("After discarding 80:", my_set)
#output:
After remove(): {40, 10, 30}
After discard(): {40, 10}
After discarding 80: {40, 10}
