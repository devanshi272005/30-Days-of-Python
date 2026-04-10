import csv

# Writing CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Devanshi", 20, 95])
    writer.writerow(["Rahul", 21, 88])

# Reading CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)