balance = 5000

def atm():
    global balance
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Choose an option: "))
        if choice == 1:
            print("Your balance is ₹", balance)
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Deposited ₹", amount)
            else:
                print("Invalid amount.")
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            elif amount > 0:
                balance -= amount
                print("Withdrawn ₹", amount)
            else:
                print("Invalid amount.")
        elif choice == 4:
            print("Thank you for using the ATM.")
            return False
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    return True

while atm():
    pass