def check_password(password):
    if len(password)<6:
        return "weak"
    elif any(char.isdigit()for char in password)and any(char.isalpha()for char in password):
        return "Strong"
    else:
        return "Medium"
print(check_password("12234546"))
    
