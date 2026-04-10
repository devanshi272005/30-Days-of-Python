import json

students = [
    {"name": "Devanshi", "marks": 95},
    {"name": "Rahul", "marks": 88}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)