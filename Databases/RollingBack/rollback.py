import sqlite3
import datetime
import pytz

# Redo changes

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY(time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') "
           "AS localtime,history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # return 1
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE name = ?", (name, ))
        row = cursor.fetchone()

        if row is not None:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}. ", end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}. ", end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        try:
            db.execute("UPDATE accounts set balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # self._balance += amount
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts set balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f"{amount / 100 :.2f} deposited.")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # self._balance -= amount
            # new_balance = self._balance - amount
            # withdraw_time = Account._current_time()
            # db.execute("UPDATE accounts set balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdraw_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
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

    rajat = Account("Rajat", 20000)
    divya = Account("Divya", 20000)
    sangeetha = Account("Sangeetha", 50000)
    pradeep = Account("Pradeep", 100000)
    deepak = Account("Deepak")

    db.close()
