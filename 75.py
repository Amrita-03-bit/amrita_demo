employees = [
    {"name": "Rahul", "salary": 50000},
    {"name": "Aman", "salary": 75000},
    {"name": "Priya", "salary": 45000},
    {"name": "Neha", "salary": 90000}
]
l=[i for i in employees if i["salary"]>60000]
for i in l:
   i["salary"]+=i["salary"]*10/100
   
print(l)