# Advanced Game Login System

import os

file_name = "users.txt"

# Register function
def register():
    username = input("Create username: ")
    password = input("Create password: ")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if len(password) >= 10 and has_upper and has_lower and has_number and has_special:
        with open(file_name, "a") as f:
            f.write(username + "," + password + "\n")
        print("User Registered ✅")
    else:
        print("Weak Password ❌")

# Login function
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    attempts = 3

    while attempts > 0:
        with open(file_name, "r") as f:
            users = f.readlines()

        for user in users:
            u, p = user.strip().split(",")
            if username == u and password == p:
                print("Login Successful 🎮")
                return

        attempts -= 1
        print(f"Wrong credentials! Attempts left: {attempts}")

        if attempts == 0:
            print("Account Locked 🔒")
            return

        username = input("Enter username: ")
        password = input("Enter password: ")

# Main menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice ❌")