from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Sita", "department": "HR", "salary": 35000},
    {"name": "Amit", "department": "IT", "salary": 45000},
    {"name": "Priya", "department": "Sales", "salary": 30000},
    {"name": "Rahul", "department": "IT", "salary": 50000}
]
it_employees = filter(
    lambda emp: emp["department"] == "IT",
    employees
)
hiked_employees = map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "salary": emp["salary"] * 1.10
    },
    it_employees
)
hiked_employees = list(hiked_employees)
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    hiked_employees,
    0
)
print("IT employees after 10% hike:")
for emp in hiked_employees:
    print(emp)
print("Total salary expenditure:", total_salary)
#output:
IT employees after 10% hike:
{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}
{'name': 'Amit', 'department': 'IT', 'salary': 49500.00000000001}
{'name': 'Rahul', 'department': 'IT', 'salary': 55000.00000000001}
Total salary expenditure: 148500.0
