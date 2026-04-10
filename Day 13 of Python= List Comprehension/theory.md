📌 What is List Comprehension?
A short and smart way to create lists in one line.

👉 Instead of writing loops, we write compact code.

🔁 Basic Syntax
[expression for item in iterable]

🧠 Example 1 – Simple List

squares = [x*x for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

🎯 Example 2 – With Condition

even = [x for x in range(10) if x % 2 == 0]
print(even)
# Output: [0, 2, 4, 6, 8]

🔤 Example 3 – Strings

chars = [ch for ch in "python"]
print(chars)
# ['p', 'y', 't', 'h', 'o', 'n']

🔄 Example 4 – Convert to Uppercase

names = ["ram", "shyam", "aman"]
upper_names = [name.upper() for name in names]
print(upper_names)

⚡ Example 5 – If-Else in List Comprehension

nums = [1, 2, 3, 4]
result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(result)

🆚 Normal Loop vs List Comprehension

❌ Normal Way

squares = []
for i in range(5):
    squares.append(i*i)

✅ List Comprehension

squares = [i*i for i in range(5)]
👉 Short + Clean + Faster