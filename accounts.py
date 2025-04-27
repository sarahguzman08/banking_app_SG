# Creating Bank Account Types

import json
import os
import random
import string

# Variables: this stores the path for the accounts data file
ACCOUNTS_DATA_FILE = "data/accounts.json"

# Functions and files: this loads existing accounts from the json file
def load_accounts():
    if not os.path.exists(ACCOUNTS_DATA_FILE):
        return [] # Branching : will return an empty list if the file does not exist
    with open(ACCOUNTS_DATA_FILE, "r") as f:
        return json.load(f)

# This saves the updated accounts into the json file
def save_accounts(accounts):
    with open(ACCOUNTS_DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# Creates a basic bank account

class Account:
    def __init__(self, account_id, user, balance=0.0):
        self.account_id = account_id # String
        self.user = user # String
        self.balance = balance # Float

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "user": self.user,
            "balance": self.balance,
            "type": self.__class__.__name__
        }
# Helper function to help find account ids associated with the username
def find_account_by_user(username):
    accounts = load_accounts()
    for account in accounts: # Loop that searches for accounts
        if account["user"] == username: # Branching to match a username
            return account
    return None

# specifying different account types

class CheckingAccount(Account):
    def __init__(self, account_id, user, balance=0.0):
        super().__init__(account_id, user, balance)

class SavingsAccount(Account):
    def __init__(self, account_id, user, balance=0.0, interest_rate=0.02):
        super().__init__(account_id, user, balance)
        self.interest_rate = interest_rate

# Includes interest rate
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["interest_rate"] = self.interest_rate
        return base_dict

# User creates a type of account

def create_account(user):
    print("\n=== Create Bank Account ===")
    print("Choose account type:")
    print("1. Checking Account")
    print("2. Savings Account")
    choice = input("Enter choice (1-2): ")

    account_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) # Generates a random 10 character acciunt ID made of capital letters and numbers.
   #Branching (if/else)
    if choice == "1":
        account = CheckingAccount(account_id, user)
    elif choice == "2":
        account = SavingsAccount(account_id, user)
    else:
        print("Invalid choice. No account created.")
        return

    accounts = load_accounts()
    accounts.append(account.to_dict()) # converts object to dictionary
    save_accounts(accounts) # saves accounts into json

    print(f"{account.__class__.__name__} created successfully! Your Account ID is {account_id}")
