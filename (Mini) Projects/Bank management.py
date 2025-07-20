from abc import ABC, abstractmethod
import os

class Account(ABC):
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class SavingsAccount(Account):
    MIN_BALANCE = 1000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance - self.MIN_BALANCE:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def create_account(self, name, opening_balance):
        if opening_balance < SavingsAccount.MIN_BALANCE:
            raise ValueError("Opening balance should be at least ₹1000.")
        account_number = 1000 + len(self.accounts) + 1
        acc = SavingsAccount(account_number, name, opening_balance)
        self.accounts[account_number] = acc
        self.save_accounts()
        return account_number

    def find_account(self, acc_no):
        return self.accounts.get(acc_no)

    def deposit(self, acc_no, amount):
        account = self.find_account(acc_no)
        if account and account.deposit(amount):
            self.save_accounts()
            return True
        return False

    def withdraw(self, acc_no, amount):
        account = self.find_account(acc_no)
        if account and account.withdraw(amount):
            self.save_accounts()
            return True
        return False

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.find_account(from_acc)
        to_account = self.find_account(to_acc)
        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                self.save_accounts()
                return True
        return False

    def check_balance(self, acc_no):
        account = self.find_account(acc_no)
        return account.get_balance() if account else None

    def save_accounts(self):
        with open("accounts.txt", "w") as f:
            for acc in self.accounts.values():
                f.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_accounts(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as f:
                for line in f:
                    acc_no, name, balance = line.strip().split(",")
                    self.accounts[int(acc_no)] = SavingsAccount(int(acc_no), name, float(balance))

def main():
    bank = Bank()

    while True:
        print("\n--- Welcome to Python Bank ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter name: ")
                balance = float(input("Enter opening balance: "))
                acc_no = bank.create_account(name, balance)
                print(f"Account created successfully! Account No: {acc_no}")

            elif choice == '2':
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                if bank.deposit(acc_no, amount):
                    print("Deposit successful.")
                else:
                    print("Deposit failed.")

            elif choice == '3':
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                if bank.withdraw(acc_no, amount):
                    print("Withdrawal successful.")
                else:
                    print("Withdrawal failed. Check balance or minimum balance limit.")

            elif choice == '4':
                acc_no = int(input("Enter account number: "))
                balance = bank.check_balance(acc_no)
                if balance is not None:
                    print(f"Current balance: ₹{balance}")
                else:
                    print("Account not found.")

            elif choice == '5':
                from_acc = int(input("From account number: "))
                to_acc = int(input("To account number: "))
                amount = float(input("Enter amount to transfer: "))
                if bank.transfer(from_acc, to_acc, amount):
                    print("Transfer successful.")
                else:
                    print("Transfer failed.")

            elif choice == '6':
                print("Thank you for using Python Bank!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("Something went wrong:", e)

if __name__ == "__main__":
    main()