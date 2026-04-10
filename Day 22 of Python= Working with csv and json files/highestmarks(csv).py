import csv

max_marks = 0
topper = ""

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Marks"]) > max_marks:
            max_marks = int(row["Marks"])
            topper = row["Name"]

print("Topper:", topper, "Marks:", max_marks)