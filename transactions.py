# transactions.py
import json
import os
import csv
from utils import format_money


ACCOUNTS_DATA_FILE = "data/accounts.json"
TRANSACTIONS_FILE = "data/transactions.csv"

def load_accounts():
    if not os.path.exists(ACCOUNTS_DATA_FILE):
        return []
    with open(ACCOUNTS_DATA_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(ACCOUNTS_DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

def find_account(account_id):
    accounts = load_accounts()
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    return None

def deposit(account_id, amount):
    accounts = load_accounts()
    for account in accounts:
        if account["account_id"] == account_id:
            account["balance"] += amount
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
    for account in accounts:
        if account["account_id"] == account_id:
            if account["balance"] >= amount:
                account["balance"] -= amount
                save_accounts(accounts)
                print(f"Withdrew {format_money(amount)} successfully!")
                print(f"New Balance: {format_money(account['balance'])}")# prints new balance in account after withdraw
                with open(TRANSACTIONS_FILE, "a", newline="") as file: # saves transaction info in transaction csv
                    writer = csv.writer(file)
                    writer.writerow([account_id, "Withdraw", amount])
            else:
                print("Insufficient funds.")
            return
    print("Account not found.")
