student1 = {"name": "dharani", "roll": 27}
student2 = student1
student3 = {"name": "satya", "roll": 72}
print(student1 == student2)
print(student1 is student2)
print(student1 == student3)
print(student1 is student3)

output:
    True
    True
    False
    False
