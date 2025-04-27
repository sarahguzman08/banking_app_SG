# Processes Transactions
# Imports built in libraries
import json
import os
import csv
from utils import format_money

# Paths to the data files
ACCOUNTS_DATA_FILE = "data/accounts.json"
TRANSACTIONS_FILE = "data/transactions.csv"

# Loads existing accounts from the files
def load_accounts():
    if not os.path.exists(ACCOUNTS_DATA_FILE):
        return []
    with open(ACCOUNTS_DATA_FILE, "r") as f:
        return json.load(f)

# saves the updated accounts in the files
def save_accounts(accounts):
    with open(ACCOUNTS_DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# finds an account by its account ID
def find_account(account_id):
    accounts = load_accounts()
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    return None

def deposit(account_id, amount):
    accounts = load_accounts()
    for account in accounts: # Loop searches for accounts
        if account["account_id"] == account_id:
            account["balance"] += amount # Variables and expressions updates balance
            save_accounts(accounts)
            print(f"Deposited {format_money(amount)} successfully!")
            print(f"New Balance: {format_money(account['balance'])}") # prints new balance in account after deposit
            with open(TRANSACTIONS_FILE, "a", newline="") as file: # saves transaction info in transaction csv
                writer = csv.writer(file)
                writer.writerow([account_id, "Deposit", amount])

            return
    print("Account not found.")

def withdraw(account_id, amount):
    accounts = load_accounts()
    for account in accounts: # Loop searches for accounts
        if account["account_id"] == account_id:
            if account["balance"] >= amount: # checks for sufficient funds 
                account["balance"] -= amount # Variables and expressions updates balance
                save_accounts(accounts)
                print(f"Withdrew {format_money(amount)} successfully!")
                print(f"New Balance: {format_money(account['balance'])}")# prints new balance in account after withdraw
                with open(TRANSACTIONS_FILE, "a", newline="") as file: # saves transaction info in transaction csv
                    writer = csv.writer(file)
                    writer.writerow([account_id, "Withdraw", amount])
            else:
                print("Insufficient funds.") # Strings message if insufficient funds
            return
    print("Account not found.") #Strings error message if account doesnt exist
