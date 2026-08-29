students = {
    101: "Ravi",
    102: "raja",
    103: "vijay"
}
removed = students.pop(102)
print("Removed:", removed)
name = students.get(105, "Key not found")
print(name)
print(students)
#output:
Removed: raja
Key not found
{101: 'Ravi', 103: 'vijay'}
