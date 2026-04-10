def login(username,password):
    if username=="admin" and password=="1234":
        return "Login successfully"
    else:
        return "Invalid Credentials"
print(login("admin", "1234"))  
  