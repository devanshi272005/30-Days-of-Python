# 🐍 Day 3 – Input & Output in Python

## 📌 1. Basic Output

```python
print("Hello, Python!")
```

---

## 📌 2. Printing Variables

```python
name = "Devanshi"
age = 20

print("Name:", name)
print("Age:", age)
```

---

## 📌 3. Using `sep` and `end`

```python
print("Python", "Java", "C++", sep=" | ")
print("Hello", end=" ")
print("World")
```

---

## 📌 4. Taking User Input

```python
name = input("Enter your name: ")
print("Welcome", name)
```

---

## 📌 5. Input as Integer

```python
num = int(input("Enter a number: "))
print("Square is:", num * num)
```

---

## 📌 6. Input as Float

```python
price = float(input("Enter price: "))
print("Price is:", price)
```

---

## 📌 7. Taking Multiple Inputs

```python
a, b = input("Enter two numbers: ").split()
print("You entered:", a, b)
```

### 👉 With Type Conversion

```python
a, b = map(int, input("Enter two numbers: ").split())
print("Sum:", a + b)
```

---

## 📌 8. Formatted Output (f-string)

```python
name = input("Enter name: ")
age = int(input("Enter age: "))

print(f"{name} is {age} years old")
```

---

## 📌 9. Simple Calculator

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

---

## 📌 10. Average of 3 Numbers

```python
a, b, c = map(int, input("Enter 3 numbers: ").split())

avg = (a + b + c) / 3
print("Average:", avg)
```

---

## 📌 11. Uppercase String

```python
text = input("Enter a string: ")
print("Uppercase:", text.upper())
```

---

## 📌 12. Check Data Type of Input

```python
x = input("Enter something: ")
print(type(x))
```
