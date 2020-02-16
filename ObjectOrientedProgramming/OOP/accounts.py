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
        self.__balance = balance
        self.transaction_list = [(Accounts._current_time(), balance)]
        print(f"The account has been created for {self.name} and balance is {self.__balance}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        print(f"Amount {amount} has been deposited in the account")
        self.show_balance()
        self.transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Accounts._current_time(), -amount))
            print(f"Amount {amount} has been withdrawn from the account")
        else:
            print("The amount has to be greater than zero no more than account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance in the account of {self.name} is {self.__balance}")

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
    deep.deposit(5000)
    deep.withdraw(1000)
    deep.show_transactions()
    # deep.show_balance()
    rajat = Accounts("Rajat", 800)
    rajat.deposit(100)
    rajat.withdraw(50)
    rajat.balance = 50
    """to prevent this from happening on line 62, we need to use two underscores in data attributes of the methods in the class.
    We have refactored the balance data attribute in the __init__ method to __balance. This process is called as
    mangling."""
    rajat.show_transactions()
    rajat.show_balance()
    print(rajat.__dict__)
