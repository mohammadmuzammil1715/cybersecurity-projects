password = input("Enter your password: ")

# Check conditions
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

# Check strength
if len(password) >= 10 and has_upper and has_lower and has_number and has_special:
    print("Strong Password")

elif len(password) >= 8 and (has_upper or has_lower) and has_number:
    print("Medium Password")

else:
    print("Weak Password")
