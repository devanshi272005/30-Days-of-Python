✅ Definition of Functions in Python

A function in Python is a block of reusable code that performs a specific task and runs only when it is called.

👉 In simple words:
A function helps you avoid repeating code and makes your program organized and efficient.

🔹 Syntax:
def function_name():
    # code block

Example:
def greet():
    print("Hello!")

greet()

🔹 Key Points:
* Defined using the keyword def
* Can take inputs (parameters)
* Can return output using return
* Helps in code reusability and modularity

Parameters are variables defined in a function . They act as a placeholder to receive values.

Arguments are the actual values passed to a function.

✅ 3. Types of Functions
🔹 (A) Built-in Functions

Predefined functions provided by Python.

Examples:

print(), len(), sum(), type()
🔹 (B) User-defined Functions

Functions created by the programmer using def.

def add(a, b):
    return a + b
🔹 (C) Anonymous Functions (Lambda)

Functions without a name.

lambda x: x*x

✅ 4. Components of a Function
🔹 (1) Function Definition
def greet():
    print("Hello")
🔹 (2) Function Call
greet()
🔹 (3) Parameters & Arguments
Parameters → variables in function definition
Arguments → values passed during function call

✅ 5. Types of Arguments
🔸 (A) Positional Arguments
def add(a, b):
    print(a + b)

add(2, 3)
🔸 (B) Keyword Arguments
add(b=3, a=2)
🔸 (C) Default Arguments
def greet(name="Guest"):
    print(name)
🔸 (D) Variable-length Arguments
*args → multiple values (tuple)
**kwargs → key-value pairs (dictionary)

✅ 6. Return Statement
Used to send value back from function
Ends execution of function
def square(x):
    return x*x

✅ 7. Scope of Variables
🔹 Local Scope

Variables inside function

🔹 Global Scope

Variables outside function

x = 10  # global

def show():
    y = 5  # local

✅ 8. Recursion (Important Theory)

A function calling itself is called recursion.

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)    

✅ 9. Docstrings

Used to describe what a function does.

def add(a, b):
    """This function returns sum of two numbers"""
    return a + b

✅ 10. Advantages of Functions
* Code reusability
* Better organization
* Easier debugging
* Saves time and effort
* Makes programs modular