class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}. ", end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount / 100 :.2f} deposited.")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount / 100 :.2f} withdrawn")
            return amount / 100
        else:
            print("Amount must be greater than zero and no more than your balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance/100:.2f}. ")


if __name__ == "__main__":
    deep = Account("Deepashu")
    deep.deposit(10000)
    deep.deposit(10)
    deep.deposit(10)
    deep.withdraw(30)
    deep.withdraw(0)
    deep.show_balance()

