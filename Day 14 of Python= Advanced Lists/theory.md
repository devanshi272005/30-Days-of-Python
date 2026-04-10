📅 Day 14 of Python – Advanced Lists (Deep Dive)

You already know basics of lists, so now we go next level 🔥

📌 1. List as Stack (LIFO)
👉 Last In First Out

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)   # [10, 20, 30]
stack.pop()
print(stack)   # [10, 20]

📌 2. List as Queue (FIFO)
👉 First In First Out

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.pop(0)
print(queue)   # [20, 30]

📌 3. Nested Lists (2D Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])   # 6

📌 4. Traversing Nested Lists
for row in matrix:
    for item in row:
        print(item, end=" ")


📌 5. List Copying (Important ⚠️)
a = [1, 2, 3]
b = a          # same reference ❌
b.append(4)
print(a)  # [1,2,3,4]

👉 Correct way:

a = [1, 2, 3]
b = a.copy()   # ✅
b.append(4)
print(a)  # [1,2,3]

📌 6. List Methods (Advanced)

nums = [5, 2, 9, 1]
nums.sort()          # sort
nums.reverse()       # reverse
nums.index(9)        # index
nums.count(2)        # count
nums.extend([10,11]) # add multiple

📌 7. List Comprehension (Quick Revision 🔥)
squares = [x*x for x in range(5)]