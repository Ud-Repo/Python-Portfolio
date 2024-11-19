class BankAccount:
    # Initialize the class using the Constructor (__init__ method)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Use a protected attribute for better encapsulation

    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self._balance += amount
        print(f"Deposited ${amount}. New Balance: ${self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self._balance}")
        else:
            print("Insufficient funds!!")

    def display_balance(self):
        print(f"Account owner: {self.owner}, Balance: ${self._balance}")


def menu():
    """Display menu options"""
    print("\n----- Bank Account Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")


if __name__ == "__main__":
    print("Welcome to the Command-Line Bank!")
    owner_name = input("Enter the account owner's name: ")
    account = BankAccount(owner_name)

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":  # Deposit
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "2":  # Withdraw
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "3":  # Display balance
            account.display_balance()

        elif choice == "4":  # Exit
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")
