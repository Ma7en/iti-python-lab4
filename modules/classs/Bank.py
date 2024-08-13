class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def get_statements(self):
        return [
            f"Account Number: {acc.account_number}, Balance: {acc.get_balance()}"
            for acc in self.accounts
        ]
