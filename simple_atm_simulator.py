# Mini Project (W1): Simple ATM Simulator
# A basic ATM program using Python functions, conditions, and a while loop.

# Initial PIN and account balance
correct_pin = 1234
balance = 5000


# Function to check the current balance
def check_balance():
    print("Your Current Balance is:", balance)


# Function to deposit money
def deposit():
    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully!")
        print("Updated Balance:", balance)
    else:
        print("Invalid amount!")


# Function to withdraw money
def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount!")
    elif amount <= balance:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance!")


# PIN-based user login
print("Welcome to Simple ATM Simulator")
pin = int(input("Enter your ATM PIN: "))

if pin == correct_pin:
    print("\nLogin Successful!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid Choice! Please try again.")

else:
    print("Incorrect PIN! Login Failed.")
