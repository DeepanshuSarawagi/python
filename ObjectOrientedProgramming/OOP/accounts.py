import datetime
import pytz


class Accounts:
    """A simple class for maintaining accounts"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f"The account has been created for {self.name} and balance is {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        print(f"Amount {amount} has been deposited in the account")
        self.show_balance()
        self.transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Accounts._current_time(), -amount))
            print(f"Amount {amount} has been withdrawn from the account")
        else:
            print("The amount has to be greater than zero no more than account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance in the account of {self.name} is {self.balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("Amount {} {} on {} and local time was {}".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    deep = Accounts("Deepanshu", 0)
    # deep.show_balance()

    deep.deposit(1000)
    deep.withdraw(500)
    deep.show_transactions()
    # deep.show_balance()
