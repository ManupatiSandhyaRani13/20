def validate_password(password):
    if len(password)<10 or len(password)>15:
        return "Password should contain min of 10 character and maximum of 15 characters"
    elif not any(char.isupper() for char in password) or not any(char.isdigit() for char in password) or not any(char.islower() for char in password) or all(char.isalnum() for char in password):
        return "Password should contain atleast one capital letter,one digit ,one lowercase letter,one special character"
    elif any(char.isspace() for char in password):
        return "Password should not contain white spaces"
    elif password[-1]=='.' or password[-1]=='@':
        return "Password should not end with a '.' and '@'"
    else:
        return "valid password"
password=input("Enter your password : ")
result=validate_password(password)
print(result)