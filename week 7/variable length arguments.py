def total_marks(*marks):
    total=sum(marks)
    average=total/len(marks)
    return total,average
#3marks
total,average=total_marks(10,20,30)
print("3marks:")
print("total:",total)
print("average:",average)
#5marks
total,average=total_marks(99,78,56,45,83)
print("5marks:")
print("total:",total)
print("average:",average)
#1 mark
total,average=total_marks(90)
print("1mark:")
print("total:",total)
print("average:",average)
#output:
3marks:
total: 60
average: 20.0
5marks:
total: 361
average: 72.2
1mark:
total: 90
average: 90.0
