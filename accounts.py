# Creating Bank Account Types

import json
import os
import random
import string

ACCOUNTS_DATA_FILE = "data/accounts.json"

def load_accounts():
    if not os.path.exists(ACCOUNTS_DATA_FILE):
        return []
    with open(ACCOUNTS_DATA_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(ACCOUNTS_DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# Creates a basic bank account

class Account:
    def __init__(self, account_id, user, balance=0.0):
        self.account_id = account_id
        self.user = user
        self.balance = balance

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
    for account in accounts:
        if account["user"] == username:
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
    if choice == "1":
        account = CheckingAccount(account_id, user)
    elif choice == "2":
        account = SavingsAccount(account_id, user)
    else:
        print("Invalid choice. No account created.")
        return

    accounts = load_accounts()
    accounts.append(account.to_dict())
    save_accounts(accounts) # saves accounts 

    print(f"{account.__class__.__name__} created successfully! Your Account ID is {account_id}")
