📌 1. What is File Handling?

👉 It allows Python to:
Read data from files 📖
Write data to files ✍️

📌 1. Why File Handling?
👉 Used to:

1. Store data permanently 💾
2. Read logs / configs
3. Work with datasets (AI/ML)
4. Build real apps

📌 2. Opening a File

file = open("example.txt", "r")

🔹 Parameters:
"example.txt" → filename
"r" → mode

📌 3. File Modes (VERY IMPORTANT)

Mode	Meaning
"r"	   Read (error if file not exist)
"w"	   Write (overwrites file)
"a"	   Append (adds content)
"x"	   Create new file
"rb"   Read binary
"wb"   Write binary

📌 4. Reading Files

🔹 (1) read() → Full file

with open("file.txt", "r") as f:
    data = f.read()
    print(data)

🔹 (2) readline() → One line

with open("file.txt", "r") as f:
    print(f.readline())

🔹 (3) readlines() → List of lines

with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)

🔹 (4) Loop through file
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

📌 5. Writing Files
🔹 Overwrite (w)

with open("file.txt", "w") as f:
        f.write("Hello World")
⚠️ Old data will be deleted

🔹 Append (a)

with open("file.txt", "a") as f:
        f.write("\nNew Line")

🔹 Write Multiple Lines

lines = ["Line1\n", "Line2\n", "Line3\n"]        
with open("file.txt", "w") as f:
        f.writelines(lines)

📌 6. File Pointer (Advanced 🔥)

👉 File cursor position

with open("file.txt", "r") as f:
    print(f.tell())   # current position
    f.read(5)
    print(f.tell())

🔹 Move pointer
with open("file.txt", "r") as f:
    f.seek(0)   # go to beginning

📌 7. Best Practice → with Statement ✅

with open("file.txt", "r") as f:
    data = f.read()
✔ Automatically closes file
✔ Prevents memory leaks

📌 8. File Exists Check

import os
if os.path.exists("file.txt"):
    print("Exists")
else:
    print("Not Found")

📌 9. Working with Binary Files

with open("image.jpg", "rb") as f:
    data = f.read()
👉 Used for images, videos, PDFs

