# Main Banking App program file for Guzman Banking
# Creating Log in process

import auth  # importing saved usernames & passwords
import accounts  # importing bank account types
import transactions  # importing transaction types

#Below will display the Main Menu Options

def show_menu(): 
    print("\n=== Welcome to the Guzman Bank ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":  # User will log in
            logged_in = auth.login() # User will attempt to log in
            if logged_in:
                user_account = accounts.find_account_by_user(logged_in) # Finds the users associated bank account
                if not user_account:
                    print("No account found for this user. Please create an account first.")
                    continue  # goes back to main menu if no account exists

# When user logs in successfully this will display an account actions menu
                while True:  
                    print("\n=== Account Actions ===")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. View Transaction Chart")
                    print("4. Logout")

                    action_choice = input("Enter your choice (1-4): ")
#Deposit money into users account
                    if action_choice == "1":
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            transactions.deposit(user_account["account_id"], amount)
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
#Withdraw money from users account
                    elif action_choice == "2":
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            transactions.withdraw(user_account["account_id"], amount)
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
 # Shows a bar chart of the transaction history by withdraw and deposit                   
                    elif action_choice == "3":
                        from plotting import plot_transactions
                        plot_transactions()  # shows chart!
# Logs user our and returns to main menu 
                    elif action_choice == "4":
                        print("Logging out...")
                        break  # Exit account actions menu back to main menu

                    else:
                        print("Invalid choice. Please enter 1, 2, 3, or 4.")

        elif choice == "2":  # Register
            registered_username = auth.register()
            if registered_username:
# Will ask to create a bank account
                create_now = input("Would you like to create a bank account now? (yes/no): ").lower()
                if create_now == "yes":
                    accounts.create_account(registered_username)

        elif choice == "3":  # Exit
            print("Thank you for using the Guzman Bank. Goodbye!")
            break

        else:
# Handles invalid input at the main menu
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()


