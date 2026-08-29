dict1 = {
    "a": 10,
    "b": 20
}
dict2 = {
    "c": 30,
    "d": 40
}
dict3 = dict1.copy()
dict3.update(dict2)
print("Using update():", dict3)
dict4 = dict1 | dict2
print("Using | operator:", dict4)
#output:
Using update(): {'a': 10, 'b': 20, 'c': 30, 'd': 40}
Using | operator: {'a': 10, 'b': 20, 'c': 30, 'd': 40}
