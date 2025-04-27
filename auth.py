# Saves usernames and passwords and uploads them to users.json file
import json
import os

USER_DATA_FILE = "data/users.json"

def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return []
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

# allows for log in and checks if user already exists

def register():
    print("\n=== Register ===")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    users = load_users()

    for user in users:
        if user["username"] == username:
            print("Username already exists. Please try again.")
            return None  # Returns none if user already exists

    users.append({"username": username, "password": password}) #If user doesnt exists
    save_users(users)
    print("Registration successful!")
    
    return username  # If registration is successful then it returns the username

def login():
    print("\n=== Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome back, {username}!")
            return username  # <<< return the username instead of just True

    print("Invalid username or password.")
    return None


