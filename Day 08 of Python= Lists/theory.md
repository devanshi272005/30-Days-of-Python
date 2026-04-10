🧠 Definition of List (Python)

A list is an ordered , mutable collection of elements where items are stored inside square brackets[] and separated by commas.

🔑 Key Properties of Lists

1. ✅ Ordered

Elements have a fixed order
Each item has a specific position (index)
numbers = [10, 20, 30]

2. ✏️ Mutable (Changeable)

You can modify, add, or remove elements
numbers = [1, 2, 3]
numbers[1] = 10
print(numbers)   # [1, 10, 3]

3. 🔁 Allows Duplicates

Lists can contain repeated values
numbers = [1, 2, 2, 3]

4. 🔀 Can Store Different Data Types

A list can contain mixed data types
mixed = [1, "Python", 3.5, True]

5. 🔢 Indexed

Each element has an index starting from 0
numbers = [10, 20, 30]
print(numbers[0])   # 10

🧩 Syntax of List
list_name = [item1, item2, item3]

🧩 1. Creating a List
numbers = [1, 2, 3, 4]
names = ["Devanshi", "Riya", "Aman"]
mixed = [1, "Python", 3.5]

🔍 2. Accessing Elements (Indexing)

👉 Index starts from 0

numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[2])   # 30

🔁 3. Negative Indexing
print(numbers[-1])   # 40
print(numbers[-2])   # 30

✂️ 4. Slicing Lists
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[::2])   # [1, 3, 5]

✏️ 5. Modifying List
numbers = [1, 2, 3]
numbers[1] = 10

print(numbers)   # [1, 10, 3]

➕ 6. Adding Elements
numbers = [1, 2]

numbers.append(3)        # add at end
numbers.insert(1, 10)    # insert at index

print(numbers)

➖ 7. Removing Elements
numbers = [1, 2, 3, 4]

numbers.remove(2)   # remove value
numbers.pop()       # remove last
numbers.pop(1)      # remove index

print(numbers)

🔄 8. Looping Through List
numbers = [1, 2, 3]

for num in numbers:
    print(num)

🧮 9. List Functions
numbers = [4, 2, 8, 1]

print(len(numbers))     # 4
print(max(numbers))     # 8
print(min(numbers))     # 1
print(sum(numbers))     # 15

🔃 10. Sorting Lists
numbers = [4, 1, 3, 2]

numbers.sort()
print(numbers)   # ascending

numbers.sort(reverse=True)
print(numbers)   # descending

🔁 11. List Comprehension (Important 🔥)
squares = [x*x for x in range(5)]
print(squares)

👉 Output:

[0, 1, 4, 9, 16]

🧩 12. Nested Lists
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])   # 2

🔍 13. Check Element in List
numbers = [1, 2, 3]

print(2 in numbers)   # True
print(5 in numbers)   # False

📊 Summary
Feature	    Description
Ordered	    Yes
Mutable	    Yes
Duplicates	Allowed
Indexing	Yes

