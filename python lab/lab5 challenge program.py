#y.dharani
# lab 5-challenge program
marks = input("Enter 3 subject marks: ").split()
m1 = int(marks[0])
m2 = int(marks[1])
m3 = int(marks[2])
average = (m1 + m2 + m3) / 3
print("Average = {:.2f}".format(average))