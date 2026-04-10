📌 1. Output in Python (print())

The print() function is used to display output on the screen.

👉 Example:

print("Hello, World!")

👉 Multiple values:

name = "Devanshi"
age = 20
print(name, age)
🔹 Customizing print()
print("Hello", "World", sep="-")   # Hello-World
print("Hello", end=" ")            # no new line
print("World")
📌 2. Input in Python (input())

The input() function is used to take input from the user.

👉 Example:

name = input("Enter your name: ")
print("Hello", name)
⚠ Important Point

👉 input() always returns string

age = input("Enter age: ")
print(type(age))   # <class 'str'>
📌 3. Type Casting with Input

To use numbers, convert input:

age = int(input("Enter age: "))
print(age + 5)

👉 Float input:

price = float(input("Enter price: "))
print(price)
📌 4. Taking Multiple Inputs
a, b = input("Enter two numbers: ").split()
print(a, b)

👉 With type conversion:

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)
📌 5. Formatted Output
🔹 Using f-strings (Best way)
name = "Devanshi"
age = 20
print(f"My name is {name} and I am {age} years old")