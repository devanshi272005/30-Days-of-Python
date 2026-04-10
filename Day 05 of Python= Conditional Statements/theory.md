🐍 Conditional Statements in Python

Conditional statements are used in programming to make decisions based on certain conditions. 
In simple words, they allow a program to choose different actions depending on whether a condition is True or False.

🔑 Types of Conditional Statements in Python

1) If statement= It is used to check a condition. If the condition evaluates to true, the code inside the if block executes.
Syntax-
if statement:
    #code
Example- 
age=20
if age>=18:
    print("Eligible for vote")

2) Else statement= It is used when we want to execute a block of code if the IF  condition is false.
Syntax-
if statement:
   #code
else statement:
   #code
Example-
age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")   

3) Elif statement= It is used when we need to check multiple condition. The program checks each condition from top to bottom.
Syntax-
if statement:
     #code
elif statememnt:
    #code
else statement:
    #code
Example-
marks=75
if marks>=90:
   print("Grade A")
elif marks>=75:
   print("Grade B")
elif marks>=60:
   print("Grade C")
else:
   print("Grade D")

🚀 Why Conditional Statements are Important?
Used in real-world applications
Helps programs become dynamic
Enables logic building
Essential for:
Login systems
Games
Calculations
AI decision making
