class BankAccount:
    # Initialize the class using the Constructor (__init__ method)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!!")

    def display_balance(self):
        print(f"Account owner: {self.owner}, Balance: ${self.balance}")

account1 = BankAccount("Davis")
account1.display_balance()
