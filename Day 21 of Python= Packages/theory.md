🔹 What is a Package in Python?

A package is a collection of modules organized in directories.

👉 In simple words:

Module = single .py file
Package = folder containing multiple modules

📁 Example structure:

my_package/
│
├── __init__.py
├── module1.py
├── module2.py
🔹 Why Use Packages?

✔ Organize large projects
✔ Avoid name conflicts
✔ Reuse code easily
✔ Improve readability

🔹 Types of Packages

1. Built-in Packages

Python already provides packages like:
math
random
os

2. User-defined Packages

Packages created by you.

🔹 Creating Your Own Package 🛠️

Step 1: Create Folder
calculator/

Step 2: Add __init__.py
(This tells Python it's a package)
calculator/
│
├── __init__.py

Step 3: Create Modules
📄 add.py

def add(a, b):
    return a + b
📄 sub.py

def sub(a, b):
    return a - b

🔹 Importing from Package

Method 1: Import entire module
import calculator.add
print(calculator.add.add(5, 3))

Method 2: Import specific function
from calculator.add import add
print(add(10, 5))

Method 3: Import all
from calculator import *

🔹 Using __init__.py
You can control what gets imported:

from .add import add
from .sub import sub
Now:

from calculator import add, sub

🔹 Installing External Packages 📥
Use pip:

pip install numpy
pip install pandas

🔹 Example of Using External Package
import math
print(math.sqrt(16))   # Output: 4.0
