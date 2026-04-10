📌 1. What are Variables?

Variables are like containers used to store data values.

👉 Example:

name = "Devanshi"
age = 20
name stores a string
age stores an integer

✔ No need to declare type (Python is dynamically typed)

📌 2. Rules for Naming Variables
Must start with a letter or _
Cannot start with a number ❌
No spaces allowed (use _)
Case-sensitive (age ≠ Age)

👉 Valid:

my_name = "Dev"
_age = 21

👉 Invalid:

2name = "Wrong"
my name = "Wrong"
📌 3. Data Types in Python
Type	Example	Description
int	10	Whole numbers
float	10.5	Decimal numbers
str	"Hello"	Text
bool	True/False	Logical values
📌 4. Checking Data Type
x = 10
print(type(x))   # Output: <class 'int'>
📌 5. Type Casting (Conversion)
a = "10"
b = int(a)   # convert string to int
print(b + 5)  # Output: 15
📌 6. Multiple Assignment
x, y, z = 1, 2, 3
print(x, y, z)
📌 7. Constants (Convention)

Python doesn’t have real constants, but we write in UPPERCASE:

PI = 3.14