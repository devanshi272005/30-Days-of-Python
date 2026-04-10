🧠 What is a Tuple?

Tuples are like lists. They are-:
* Ordered 
* Immutable
* Mixed datatypes such as string, integer, and float.

They are stored in () paranthesis.

🧩 1. Creating a Tuple
t = (1, 2, 3)
print(t)

For a single element, we use a comma to represent it as tuple.
 class=("Alex",)
 print(type(class))

 🔍 2. Accessing Elements (Indexing)
t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40

✂️ 3. Slicing Tuple
t = (1, 2, 3, 4, 5)

print(t[1:4])   # (2, 3, 4)
print(t[:3])    # (1, 2, 3)

❌ 4. Immutability (Very Important)
t = (1, 2, 3)

# t[1] = 10  ❌ Error

👉 You cannot change tuple elements

➕ 5. Tuple Operations
1) Concatenation= We use + operator to add two tuples.
2) Repetition= We use * operator to repeat the elements of the tuples.
Example-
t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)   # (1, 2, 3, 4)
print(t1 * 2)    # (1, 2, 1, 2)

🧠 What is Sorting?

👉 Sorting means arranging data in order

Ascending → small to big
Descending → big to small
Sort values in a tuple and save it to a new tuple.
Example-
 age=(12,58,56,45)
 sorted_age=sorted(age)   # using sorted() function
 print(sorted_age)    #(12,45,56,58)

🔍 7. Tuple Functions
t = (4, 2, 8, 1)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))

🔄 8. Convert Tuple ↔ List
t = (1, 2, 3)

lst = list(t)
lst.append(4)

t = tuple(lst)
print(t)

🧩 9. Nested Tuple
t = ((1, 2), (3, 4))

print(t[0][1])   # 2

🔐 10. Tuple Packing & Unpacking
t = (1, 2, 3)   # packing

a, b, c = t     # unpacking

print(a, b, c)

🔍 11. Check Element Exists
t = (1, 2, 3)

print(2 in t)   # True

