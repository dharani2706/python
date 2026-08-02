#dharani satya
#B4.1 - logical operators
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)
# Enter percentage: 80
# Enter attendance: 95
# Eligible for scholarship: True