🔁 Definition of Loops in Python

A loop in Python is a programming construct that allows you to execute a block of code repeatedly as long as a condition is true or for a fixed number of times.

📌 In Simple Words:

A loop helps you avoid writing the same code again and again by automating repetition.

🧠 Formal Definition:

A loop is a control structure that repeatedly executes a set of statements until a specified condition is met or for a defined sequence.

🔄 Types of Loops:
1) for loop → Repeats code for a fixed sequence.
  Syntax=
  for variable in sequence:
    # code block
range()function=> Used with for loop to generate numbers.  
     range(start, stop, step)

2) while loop → repeats code based on a condition.
    Syntax=
    while condition:
    # code block

🔄 2. Loop Control Statements

These help you control loop execution.

📌 Break

Stops the loop completely.

for i in range(1, 10):
    if i == 5:
        break
    print(i)

📌 Continue

Skips the current iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

📌 Pass

Does nothing (placeholder).

for i in range(5):
    pass    

🔁 3. Nested Loops

A loop inside another loop.

🔹 Example:
# Print a simple pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
        
