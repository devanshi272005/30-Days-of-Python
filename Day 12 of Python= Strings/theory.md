📌 1. What is a String?

A string is a sequence of characters enclosed in quotes.

👉 Example:

name = "Devanshi"
Can use " " or ' '
Immutable (cannot change directly)

🧠 Real-Life Understanding
💬 Messages → "Hello"
📧 Emails → "example@gmail.com
"
🧾 Names → "Rahul"

🧾 2. Creating Strings
a = "Hello"
b = 'Python'
c = """Multi-line
String"""

🔑 3. String Indexing
text = "Python"

print(text[0])   # P
print(text[-1])  # n

👉 Index starts from 0

✂️ 4. String Slicing
text = "Python"

print(text[0:3])   # Pyt
print(text[:4])    # Pyth
print(text[2:])    # thon

🔄 5. String Operations
➕ Concatenation
a = "Hello"
b = "World"

print(a + " " + b)
🔁 Repetition
print("Hi " * 3)

🔍 6. String Methods (Very Important 🔥)
Method	Use
.lower()	lowercase
.upper()	uppercase
.strip()	remove spaces
.replace()	replace text
.split()	convert to list
.find()	find index
.count()	count occurrences

✔️ Examples
text = "  Python Programming  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Python", "Java"))

🔄 7. Looping Through String
for char in "Python":
    print(char)

🔎 8. Checking in String
text = "Python"

print("Py" in text)   # True

🧠 9. String Formatting
✔️ Old Style
name = "Devanshi"
print("Hello", name)
✔️ f-String (Best 🔥)
name = "Devanshi"
age = 20

print(f"My name is {name} and I am {age}")

⚠️ 10. Important Concept (Immutability)
text = "Python"

# ❌ Not allowed
# text[0] = "J"

# ✔️ Correct way
text = "Jython"

