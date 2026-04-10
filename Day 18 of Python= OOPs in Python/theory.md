OOP in Python (Theory in Detail) 🚀

📌 1. What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects and classes instead of just functions and logic.

👉 It helps in:

Code reusability
Modularity
Real-world modeling

📌 2. Core Concepts of OOP (4 Pillars 🔥)

🧱 1. Encapsulation

👉 Wrapping data + methods into one unit (class)
👉 Also used to hide data (data hiding)

🔹 Types:
Public → accessible anywhere
Protected (_var) → internal use
Private (__var) → not directly accessible

💡 Why important?

Prevents accidental modification
Improves security

🧬 2. Inheritance

👉 One class inherits properties and methods of another class

🔹 Types of Inheritance:
Single
Multiple
Multilevel
Hierarchical

💡 Advantages:
Code reuse
Reduces redundancy

🎭 3. Polymorphism

👉 “Many forms”
👉 Same method behaves differently for different objects

🔹 Types:
Method Overriding (most common in Python)
Method Overloading (limited in Python)

💡 Example idea:
sound() → dog barks, cat meows

🎯 4. Abstraction

👉 Hiding internal details and showing only necessary features

🔹 Achieved using:
Abstract classes (ABC)
Abstract methods

💡 Why?
Simplifies complex systems
Focus on what, not how

📌 3. Class vs Object (Deep Understanding)\

Feature	Class	Object
Definition	Blueprint	Instance
Memory	No memory allocated	Memory allocated
Example	Car	MyCar

👉 Think:

Class = Design of house
Object = Actual house

📌 4. Constructor (__init__)

👉 Special method that runs automatically when object is created

💡 Purpose:
Initialize object data

🔹 Types:
Default constructor
Parameterized constructor

📌 5. self Keyword
👉 Refers to current instance of class

💡 Why needed?
To access instance variables
To differentiate local and instance variables

📌 6. Types of Variables in OOP
🔹 Instance Variables
Unique for each object
Defined using self

🔹 Class Variables
Shared among all objects
Defined inside class but outside methods

📌 7. Types of Methods
🔹 Instance Method
Works with object data

🔹 Class Method
Uses @classmethod
Works with class variables

🔹 Static Method
Uses @staticmethod
No access to class/object data

📌 8. Data Hiding (Important ⚠️)
👉 Achieved using:
__variable (name mangling)

💡 Benefit:
Prevent direct access
Controlled access via methods

📌 9. Method Overriding
👉 Child class modifies parent method

💡 Key Point:
Same method name
Different implementation

📌 10. Advantages of OOP

✔ Code reusability
✔ Easy maintenance
✔ Better organization
✔ Scalable projects

📌 11. Disadvantages of OOP

❌ Requires planning
❌ Slightly slower execution
❌ More complex than procedural

