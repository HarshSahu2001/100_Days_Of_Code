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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
power = True


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {resources[item]}.")
            return False
        return True


def process_coins():
    Total = int(input("How many quarters: "))
    Total += int(input("How many dimes: "))
    Total += int(input("How many nickles: "))
    Total += int(input("How many Pennies: "))
    return Total


def is_transanction_succesful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here's your {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here's your {drink_name}. Enjoy!")


while power:
    person_choice = input(
        "What would you like? espresso/latte/cappuccino: ").lower()
    if person_choice == "off":
        power = False
    elif person_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
    else:
        drink = MENU[person_choice]
        if is_resource_sufficient():
            payment = process_coins()
            if is_transanction_succesful(payment, drink["cost"]):
                make_coffee(person_choice, drink["ingredients"])
