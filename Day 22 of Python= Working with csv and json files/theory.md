🔷 1. Introduction to Data Formats

In programming, data formats are used to store and exchange data between systems.

The two most commonly used formats are:

CSV (Comma Separated Values) → used for simple tabular data
JSON (JavaScript Object Notation) → used for structured and complex data

👉 Real-world usage:

CSV → Excel files, reports
JSON → APIs, web applications

🔷 2. CSV (Comma Separated Values)
🔹 Definition
CSV is a plain text format where data is stored in rows and columns, separated by commas.

Example:

Name,Age,Marks
Devanshi,20,95
Rahul,21,88

🔹 Key Characteristics

Simple and easy to use
Stores data in tabular form
Each line represents a record
Values are separated by commas
Does not support nested data

🔹 Advantages

✔ Easy to read and write
✔ Compatible with Excel and spreadsheets
✔ Lightweight 

🔹 Limitations

❌ Cannot store complex/nested data
❌ No support for data types (everything is treated as text)
❌ No built-in security

🔹 CSV in Python (Theory)

Python provides a built-in csv module to work with CSV files.

Main functions:

csv.reader() → reads data
csv.writer() → writes data
csv.DictReader() → reads as dictionary
csv.DictWriter() → writes dictionary

🔹 Internal Working

When a CSV file is read:

Each line is split using commas
Data is converted into a list or dictionary

Example:

"Devanshi,20,95" → ["Devanshi", "20", "95"]ht (small file size)
✔ Fast processing

🔷 3. JSON (JavaScript Object Notation)

🔹 Definition
JSON is a structured data format that stores data as key-value pairs.

Example:

{
  "name": "Devanshi",
  "age": 20,
  "marks": 95
}

🔹 Key Characteristics

Stores data in structured format
Supports nested (hierarchical) data
Human-readable
Language-independent

🔹 Data Types in JSON

JSON supports:

String
Number
Boolean
Array (list)
Object (dictionary)
Null

🔹 Advantages
✔ Can store complex and nested data
✔ Widely used in APIs
✔ Easy to parse and generate
✔ Structured format

🔹 Limitations
❌ Larger file size compared to CSV
❌ Slower for very large data
❌ Does not support comments

🔹 JSON in Python (Theory)

Python uses the built-in json module.

Main functions:

json.load() → read from file
json.dump() → write to file
json.loads() → string → Python object
json.dumps() → Python object → string

🔹 Internal Working
JSON is converted into Python data structures:

JSON Type	  Python Type
Object	       Dictionary
Array	       List
String	       String
Number	      int/float
Boolean	      True/False

🔷 4. CSV vs JSON (Comparison)

| Feature     | CSV            | JSON           |
| ----------- | -------------- | -------------- |
| Structure   | Tabular        | Hierarchical   |
| Complexity  | Simple         | Complex        |
| Data Types  | Text only      | Multiple types |
| Use Case    | Excel, reports | APIs, web apps |
| Readability | Very easy      | Moderate       |

🔷 5. When to Use CSV vs JSON

✅ Use CSV when:

Data is simple and tabular
You are working with Excel
No nested structure is needed

✅ Use JSON when:

Data is complex or nested
You are working with APIs
You need structured data

🔷 6. Real-Life Applications

📊 CSV:

Student records
Attendance systems
Sales reports

🌐 JSON:

Web APIs
Mobile apps
Configuration files

🔷 7. Important Exam Points 📌

CSV is a flat file format
JSON is a structured format
CSV does not support nesting
JSON supports key-value pairs
Python provides built-in modules (csv, json)

📄 Part 1: CSV Files

🔸 Reading CSV File

import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

🔸 Writing CSV File

import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Devanshi", 20, 95])

🔸 Using DictReader (Best Way)
import csv    
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
       print(row["Name"], row["Marks"])

📦 Part 2: JSON Files

🔸 Reading JSON File

import json
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])

🔸 Writing JSON File

import json
data = {
    "name": "Devanshi",
    "age": 20,
    "marks": 95
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

🔸 Convert Python ↔ JSON

import json  
# Python → JSON string
json_data = json.dumps({"a": 1})
print(json_data)   
# JSON → Python
python_data = json.loads(json_data)
print(python_data)