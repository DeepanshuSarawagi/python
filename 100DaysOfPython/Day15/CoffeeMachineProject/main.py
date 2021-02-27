MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns when order can be made or False when ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough {}".format(item))
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""

    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    """Return True when payment is accepted or Return False if payment is insufficient"""
    if money_received >= cost_of_drink:
        return True
    else:
        print("Sorry that's not enough money! Money refunded")
        return False


is_on = True

while is_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino)? ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("Water: {}ml".format(resources["water"]))
        print("Milk: {}ml".format(resources["milk"]))
        print("Coffee: {}g".format(resources["coffee"]))
        print("Money: ${}".format(profit))
    else:
        drink = MENU[choice]
        if print(is_resource_sufficient(drink["ingredients"])):
            payment = process_coins()
