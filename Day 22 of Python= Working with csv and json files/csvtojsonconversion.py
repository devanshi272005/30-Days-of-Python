import csv
import json

data = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("Conversion successful!")