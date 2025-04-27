# plotting.py

import matplotlib.pyplot as plt
import csv

TRANSACTIONS_FILE = "data/transactions.csv"

def plot_transactions():
    amounts = []
    actions = []

    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header if you have one
            for row in reader:
                actions.append(row[1])
                amounts.append(float(row[2]))
    except FileNotFoundError:
        print("No transactions to plot.")
        return

    if not amounts:
        print("No transactions to plot.")
        return

    plt.bar(actions, amounts)
    plt.title("Transactions Overview")
    plt.xlabel("Action")
    plt.ylabel("Amount ($)")
    plt.show()
