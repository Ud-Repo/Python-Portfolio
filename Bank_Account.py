#Create a bank account by creating a dictionary
def create_account(owner, balance=0):
    return {"owner":owner, "balance" : balance}
def deposit(account, amount):
    account["balance"] += amount
    print (f"Deposited ${amount}. New balance : ${account['balance']}")
    def withdraw(account, amount):
        if amount <= account["balance"]:
            print (f"Withdrew ${amount}. New balance : ${account['balance']}")
 #pass [used when you dont want to put in a value yet.]
 