marks = [40, 55, 70, 30, 90]

# Passed students
passed = list(filter(lambda x: x >= 50, marks))

# Add grace marks (+5)
updated = list(map(lambda x: x + 5, passed))

print(updated)
