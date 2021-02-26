# This is the proposed solution by the instructor

from game_data import data
import random

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)


def format_data(account):

    account_name = account["name"]
    account_decr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_decr} from {account_country}"


print("Compare A: {}".format(format_data(account_a)))
print("Compare B: {}".format(format_data(account_b)))
