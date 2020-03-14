import sqlite3
import datetime
import pytz

db = sqlite3.connect("accounts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions(time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name, ))
        row = cursor.fetchone()

        if row is not None:
            self.name, self._balance = row
            print(f"Account retrieved for {self.name}. ", end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name} ", end=' ')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f"{amount} deposited.")
        return self._balance

    def withdraw(self, amount) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
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
    deep.deposit(10)
    deep.deposit(65)
    deep.deposit(10)
    deep.withdraw(50)
    deep.withdraw(0)
    deep.show_balance()

    rajat = Account("Rajat", 100)
    divya = Account("Divya", 100)
    sangeetha = Account("Sangeetha", 500)
    pradeep = Account("Pradeep", 1000)
    deepak = Account("Deepak", 500)

    db.close()
