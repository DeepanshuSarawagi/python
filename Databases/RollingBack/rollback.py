import sqlite3

db = sqlite3.connect("accounts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions(time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name, ))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print(f"Account retrieved for {self.name}")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}", end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount} deposited.")
        return self._balance

    def withdraw(self, amount) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn.")
            return amount
        else:
            print("Amount must be greater than zero and no more than balance.")
            return 0.0

    def show_balance(self):
        print(f"Balance in the account {self.name} is {self._balance}")


if __name__ == "__main__":
    deep = Account("Deepanshu")
    deep.deposit(100)
    deep.deposit(0.10)
    deep.deposit(0.65)
    deep.deposit(0.10)
    deep.withdraw(0.50)
    deep.withdraw(0)
    deep.show_balance()
