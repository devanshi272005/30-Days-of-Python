try:
    password = input("Enter password: ")

    if password != "1234":
        raise ValueError("Wrong password")

    print("Login successful")

except ValueError as e:
    print(e)
    