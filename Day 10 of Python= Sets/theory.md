📌 What is a Set?

It is an unordered collection of unique object. All the elements inside a set are immutable(int,str,tuple) but the set itself is mutable. Repetition is not allowed. It is represented in curly braces{}.
Example name={"alice","bob","charlie"}
        print(name)

Create an empty set=> my_set=set()
                      print(my_set)

🔑 Important Properties
* No duplicates allowed
* No indexing (can't access by position)
* Mutable (you can add/remove items)

➕ Adding Elements
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

➖ Removing Elements
my_set.remove(2)   # error if not present
my_set.discard(5)  # no error

⚙️ Set Operations (Most Important 🔥)

1. Union (Combine sets)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # {1,2,3,4,5}
print(a.union(b))   #{1,2,3,4,5}

2. Intersection (Common elements)
print(a & b)   # {3}
print(a.intersection(b))  #{3}

3. Difference
print(a - b)   # {1,2}
print(a.difference(b))   #{1,2}
print(b.difference(a))   #{4,5}

4. Symmetric Difference
print(a ^ b)   # {1,2,4,5}
print(a.symmetric_difference(b))    #{1,2,4,5}

