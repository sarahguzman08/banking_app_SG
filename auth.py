# Saves usernames and passwords and uploads them to users.json file
#Importing built in libraries
import json
import os

# Variables: Storing the path to the data file
USER_DATA_FILE = "data/users.json"

# loads existing users from the json files
def load_users():
    if not os.path.exists(USER_DATA_FILE): # Checks if file exists
        return [] # returns an empty list if the file doesnt exist
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

# saves updates user list in the json file
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

# allows for log in and checks if user already exists

def register():
    print("\n=== Register ===")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    users = load_users()

# checks if username already exists
    for user in users:
        if user["username"] == username:
            print("Username already exists. Please try again.")
            return None  # Returns none if user already exists
# Adds a new user 
    users.append({"username": username, "password": password}) #If user doesnt exists
    save_users(users)
    print("Registration successful!")
    
    return username  # If registration is successful then it returns the username

# Allows an existing user to log in
def login():
    print("\n=== Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users = load_users()

# checcks if username and password match
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome back, {username}!")
            return username  # <<< return the username instead of just True

    print("Invalid username or password.") # string output error message
    return None


