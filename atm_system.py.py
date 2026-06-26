import random

class ATM:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def account_detail(self):
        print(f"\n--- ACCOUNT DETAIL ---")
        print(f"Holder: {self.name.upper()}")
        print(f"Account: {self.account_no}")
        print(f"Balance: {self.balance}\n")
        
    def check_balance(self):
        print(f"\nAvailable balance: {self.balance}\n")
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: {amount}")
            print(f"New Balance: {self.balance}\n")
        else:
            print("Invalid deposit amount!\n")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient fund!")
            print(f"Your balance is {self.balance} only.")
        elif amount <= 0:
            print("Invalid amount!\n")
        else:
            self.balance -= amount
            print(f"\n{amount} withdrawal successful!")
            print(f"Current balance: {self.balance}\n")
            
    def transaction(self):
        while True:
            print("--- TRANSACTION MENU ---")
            print("1. Account Detail | 2. Check Balance | 3. Deposit | 4. Withdraw | 5. Exit")
            try:
                option = int(input("Choose an option: "))
                if option == 1: self.account_detail()
                elif option == 2: self.check_balance()
                elif option == 3: self.deposit(int(input("Deposit amount: ")))
                elif option == 4: self.withdraw(int(input("Withdraw amount: ")))
                elif option == 5:
                    print(f"\n--- RECEIPT ---")
                    print(f"Trans No: {random.randint(10000, 99999)}")
                    print(f"Holder: {self.name.upper()} | Balance: {self.balance}")
                    print("Thanks for banking with us!")
                    break
                else: print("Enter 1-5 only!")
            except ValueError:
                print("Error: Invalid input, please enter numbers only.\n")

# Main Execution
print("**************** WELCOME TO BANK OF DELHI ****************")
name = input("Enter your name: ")
acc_no = int(input("Enter account number: "))
print("Account created successfully!\n")
 
user_atm = ATM(name, acc_no)
user_atm.transaction()