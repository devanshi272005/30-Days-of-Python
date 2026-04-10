contacts = {
    "Mom": 9876543210,
    "Dad": 9123456780
}

name = input("Enter name: ")

if name in contacts:
    print("Number:", contacts[name])
else:
    print("Not found")