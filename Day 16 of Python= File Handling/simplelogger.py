log = input("Enter log message: ")

with open("log.txt", "a") as f:
    f.write(log + "\n")