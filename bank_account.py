# Bank Account Class
# Features: deposit, withdraw, and display balance

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                self.balance += amount
                print(f"Rs. {amount:.2f} deposited successfully.")
        except ValueError:
            print("Please enter a valid number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"Rs. {amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Please enter a valid number.")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Available balance: Rs. {self.balance:.2f}")


# Main program
name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = input("Enter amount to deposit: ")
        account.deposit(amount)
    elif choice == "2":
        amount = input("Enter amount to withdraw: ")
        account.withdraw(amount)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Thank you for using our bank service.")
        break
    else:
        print("Invalid choice. Please try again.")
