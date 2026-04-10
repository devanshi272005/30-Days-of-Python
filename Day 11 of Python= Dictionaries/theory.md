📌 1. What is a Dictionary?

A dictionary is a collection of key–value pairs used to store data in a structured way.

👉 General form:
{key: value}

🔑 Keys → Unique, immutable (string, int, tuple)
📦 Values → Any data type (list, string, int, even another dictionary)

🧠 Real-Life Understanding
📱 Contacts → "Rahul": 9876543210
🎓 Student Record → "Roll101": 85
📖 Dictionary → "Python": "Programming Language"

🧾 2. Creating Dictionaries

✔️ Method 1: Using {}
student = {
    "name": "Devanshi",
    "age": 20,
    "course": "BTech"
}
✔️ Method 2: Using dict()
student = dict(name="Devanshi", age=20)
✔️ Method 3: Empty Dictionary
data = {}

🔑 3. Accessing Values
✔️ Using Key
print(student["name"])

⚠️ Error if key not present

✔️ Using .get() (Safe Method)
print(student.get("age"))
print(student.get("marks", "Not Found"))

➕ 4. Adding & Updating Elements
student["age"] = 21       # update
student["city"] = "Delhi" # add new

➖ 5. Removing Elements
student.pop("course")     # removes key
del student["age"]        # deletes key
student.clear()           # removes all

🔄 6. Looping Through Dictionary
✔️ Keys Only
for key in student:
    print(key)
✔️ Values Only
for value in student.values():
    print(value)
✔️ Key-Value Pair
for key, value in student.items():
    print(key, ":", value)

📚 7. Important Dictionary Methods
Method	     Description
.keys()	     Returns all keys
.values()	 Returns all values
.items()	 Returns key-value pairs
.update()	 Updates dictionary
.pop()	     Removes element
.clear()	 Clears dictionary

🧪 8. Nested Dictionary (Very Important 🔥)
students = {
    "student1": {"name": "Rahul", "marks": 85},
    "student2": {"name": "Aman", "marks": 90}
}

print(students["student1"]["name"])

👉 Used in real databases & APIs

🧠 9. Dictionary Comprehension

👉 Short way to create dictionary

squares = {x: x*x for x in range(1, 6)}
print(squares)

🔍 10. Membership Checking
if "name" in student:
    print("Key exists")

🔄 11. Copying Dictionary
new_student = student.copy()

⚠️ 12. Important Rules
Keys must be unique
Keys must be immutable (no list allowed ❌)
Values can be anything
Dictionaries are mutable



