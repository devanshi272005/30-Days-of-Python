📦 Definition of Modules in Python

A module in Python is a file (.py) that contains a collection of functions, variables, and classes, which can be imported and reused in another Python program.

🔹 Simple Definition

👉 A module is a Python file used to organize and reuse code.

🔹 Example
# mymodule.py
def greet():
    print("Hello, welcome!")

👉 Using it in another file:
import mymodule
mymodule.greet()

🔹 Key Points

A module = .py file
Helps in code reusability
Improves readability and structure
Can be built-in or user-defined

 Types of Modules
1. Built-in Modules
Already available in Python
Examples:

math

random

datetime

2. User-defined Modules
Created by you
Example: numericcalculation.py

🔹 Ways to Import Modules
1. Normal Import

import math
print(math.sqrt(16))

2. Import with Alias

import math as m
print(m.sqrt(25))

3. Import Specific Functions

from math import sqrt
print(sqrt(36))

4. Import Everything

from math import *
⚠️ Not recommended

🔹 Module Search Path (Very Important Theory 🔥)
Python searches modules in:

Current directory
Installed libraries
System paths

Check path:

import sys
print(sys.path)

🔹 Advantages of Modules

✔ Code reusability
✔ Better structure
✔ Easy maintenance
✔ Faster development

