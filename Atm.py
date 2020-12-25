# -----------------------------------------------------------------------------------------------------------------------------------------#
# Author: JM Cameron

# Import the account and customer classes.
import account
import customer


# This is the main function of the program.
def main():
    # Print formatted header row for the program.
    print('\n', '-' * 30, "Welcome to Bank of Python", '-' * 30)

    # Create a dictionary for stored balances of the three previous customers.
    accounts = {'JOHN': 5000, 'JANE': 5000, 'JOE': 5000}

    # Obtain input from the user.
    # Greet user, and display saved balance. If user's name doesn't exist, open a new account with 10 USD sign up gift.
    name = input("\nPlease enter your name: ").upper()
    if accounts.get(name) is None:
        accounts.update({name: 10})
        print("\nThank you for being a new customer " + name + ", the balance in your new account is ",
              accounts.get(name), "USD.")
    else:
        print("\nHello " + name + ", the balance in your account is ", accounts.get(name), "USD.")

    # This is a repeating while loop to accept as many transactions as the user would like enter. 
    repeat = "yes"
    while repeat == "yes":

        transaction_type = input(
            "\nWhat type of transaction would you like? Please enter deposit or withdraw: ").upper()
        currency = input("Please enter your currency. It can be USD, EUR, or CAD: ").upper()

        # Assign variables to read into the class functions.
        user = customer.Customer()
        user.set_name(name)
        balance = accounts.get(name)
        assigned_account = account.Account(name, balance)

        # Determine if the transaction amount will add or subtract from the balance.
        # Exception handlers if amount entered is not a number.
        if transaction_type == "DEPOSIT":
            try:
                amount = int(input("Please enter the deposit amount: "))
                # Pass variables into the account class functions. Save updated balance back to dictionary.
                amount_usd = assigned_account.convert(currency, amount)
                updated_balance = assigned_account.update(amount_usd)
                print("\nThank you " + user.get_name() + ", your updated balance is: " + str(updated_balance) + " USD.")
                accounts[name] = updated_balance
            except:
                print("The input was invalid.")
        elif transaction_type == "WITHDRAW":
            try:
                amount = -1 * int(input("Please enter the withdrwal amount: "))
                # If function for withdrawl amount larger than balance.
                # Pass variables into the account class functions. Save updated balance back to dictionary.
                if amount + balance >= 0:
                    amount_usd = assigned_account.convert(currency, amount)
                    updated_balance = assigned_account.update(amount_usd)
                    print("\nThank you " + user.get_name() + ", your updated balance is: " + str(
                        updated_balance) + " USD.")
                    accounts[name] = updated_balance
                else:
                    print("Insufficient funds, you cannot withdraw that amount. Your balance is " + str(balance))
            except:
                print("The input was invalid.")
        else:
            print("The input was invalid.")

        # This repeater variable allows the user to run the program again or terminate.
        repeat = input("\nPlease enter 'yes' if you would like to make another transaction: ")

    # This line prints a formatted footer row for the program.
    print('\n', '-' * 40, "Goodbye", '-' * 39)


# The main function is called and all of the above code is run.
main()

# Date: November 2020
# -----------------------------------------------------------------------------------------------------------------------------------------#
