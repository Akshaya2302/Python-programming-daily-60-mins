employees = {
101: {"name": "Ravi", "salary": 25000},
102: {"name": "Anita", "salary": 40000},
103: {"name": "Kiran", "salary": 30000}
}
eid = int(input("Enter Employee ID: "))

if eid in employees:
    print(employees[eid])
else:
    print("Employee Not Found")

        
highest = max(employees, key=lambda x: employees[x]["salary"])
lowest = min(employees, key=lambda x: employees[x]["salary"])
print("Highest Salary:", employees[highest])
print("Lowest Salary:", employees[lowest])