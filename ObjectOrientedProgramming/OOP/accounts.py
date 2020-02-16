class Accounts:
    """A simple class for maintaining accounts"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"The account has been created for {self.name} and balance is {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        print(f"Amount {amount} has been deposited in the account and balance is {self.balance}")

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        print(f"Amount {amount} has been withdrawn from the account and balance is {self.balance}")

    def show_balance(self):
        print(f"Balance in the account is {self.balance}")


if __name__ == "__main__":
    deep = Accounts("Deepanshu", 0)
    deep.show_balance()

    deep.deposit(1000)
    deep.withdraw(500)
    deep.show_balance()
