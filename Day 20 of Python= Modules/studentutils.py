def average(marks):
    return sum(marks) / len(marks)

def is_pass(marks):
    return average(marks) >= 40

def grade(marks):
    avg = average(marks)
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
import studentutils

marks = [80, 70, 90, 60]

print(studentutils.average(marks))
print(studentutils.is_pass(marks))
print(studentutils.grade(marks))    