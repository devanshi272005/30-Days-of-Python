with open("source.txt", "r") as src:
    data = src.read()

with open("dest.txt", "w") as dest:
    dest.write(data)