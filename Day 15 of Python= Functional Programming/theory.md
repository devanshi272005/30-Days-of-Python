Lambda, Map, Filter (Functional Programming)

This is used a LOT in:
Data Science 📊
AI/ML 🤖
Clean & short code ✨

📌 1. Lambda Function (Anonymous Function)
👉 A function without name

🔹 Syntax
lambda arguments: expression

🎯 Example 1

square = lambda x: x * x
print(square(5))   # 25🎯 

Example 2

add = lambda a, b: a + b
print(add(3, 4))   # 7

⚡ Why Lambda?
👉 Used when:
Function is small
Needed only once
Want short code

📌 2. map() Function

👉 Applies a function to all items in a list

🔹 Syntax
map(function, iterable)

🎯 Example

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

🧠 Without map (normal way)

result = []
for i in nums:
    result.append(i*i)
👉 map makes it short & clean

 3. filter() Function

👉 Filters elements based on condition

🔹 Syntax
filter(function, iterable)

🎯 Example

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

