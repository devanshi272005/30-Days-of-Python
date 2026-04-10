📌 1. What is an Exception?

👉 An error that occurs during program execution

🔹 Example:
print(10 / 0)   # ❌ ZeroDivisionError

📌 2. Why Exception Handling?

👉 Without it → program crashes ❌
👉 With it → program continues ✅

📌 3. try & except

🔹 Syntax
try:
    # risky code
except:
    # error handling
🎯 Example
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Error occurred!")

📌 4. Catch Specific Errors (BEST PRACTICE ✅)

    try:
        x = int(input("Enter number: "))
        print(10 / x)
    
    except ZeroDivisionError:
        print("Cannot divide by zero")
    
    except ValueError:
        print("Invalid input")

📌 5. Multiple Exceptions in One Line

try:
    x = int(input())
    print(10 / x)

except (ZeroDivisionError, ValueError):
    print("Error occurred")

📌 6. else Block

👉 Runs if no error occurs
try:
  x = int(input())
        print(10 / x)
    
except:
     print("Error")
    
else:
     print("Success!")

📌 7. finally Block (VERY IMPORTANT 🔥)

👉 Always runs (error or not)

     try:
         f = open("file.txt")
     except:
         print("File not found")
     
     finally:
         print("This always runs")

📌 8. Multiple Exceptions in One Line

try:
    x = int(input())
    print(10 / x)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division error")


📌 9. Raising Exceptions

👉 You can create your own errors

age = int(input("Enter age: "))

if age < 18:
    raise Exception("Not eligible!")

📌 10. Custom Exception (Advanced 🔥)

class MyError(Exception):
    pass
raise MyError("This is custom error")

