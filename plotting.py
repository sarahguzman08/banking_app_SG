# Transaction visualization
# Importing libraries
import matplotlib.pyplot as plt
import csv

# path to the data file
TRANSACTIONS_FILE = "data/transactions.csv"

def plot_transactions():
    amounts = []
    actions = []

# Reads transactions from files
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header if you have one
            # Loops each row in the csv
            for row in reader:
                actions.append(row[1])
                amounts.append(float(row[2]))
    except FileNotFoundError:
        # Exception handling if file doesnt exist
        print("No transactions to plot.")
        return

    if not amounts:
        print("No transactions to plot.")
        return

#Creates the bar chart
    plt.bar(actions, amounts)
    plt.title("Transactions Overview")
    plt.xlabel("Action")
    plt.ylabel("Amount ($)")
    plt.show()
