# Create a bank account by creating a dictionary
def create_account(owner, balance=0):
    return {"owner": owner, "balance": balance}

# Deposit into the account
def deposit(account, amount):
    account["balance"] += amount
    print(f"Deposited ${amount}. New balance: ${account['balance']}")

# Withdraw from the account
def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrew ${amount}. New balance: ${account['balance']}")
    else:
        print("Insufficient funds!!")

# Pass [used when you don't want to put in a value yet.]
def display_balance(account):
    print(f"Account owner: {account['owner']}, Balance: ${account['balance']}")

# Main
account1 = create_account("Davis")
# Check the account
# print(account1)
display_balance(account1)
deposit(account1, 1000)
withdraw(account1, 500)
print(type(account1))
