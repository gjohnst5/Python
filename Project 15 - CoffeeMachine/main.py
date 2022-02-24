
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

bank = {
    "money": 0.0}


def decrease_resources(order):
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]


def process_order(order):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    cost = MENU[order]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    if cost > total:
        print("Sorry that's not enough money. Money refunded.")
    elif cost < total:
        decrease_resources(order)
        bank["money"] += cost
        print("Here is $" + str(float(total - cost)) + " in change.\nHere is your " + order + " ☕. Enjoy!")
    else:
        decrease_resources(order)
        bank["money"] += cost
        print("Thank you!\n Here is your " + order + " ☕. Enjoy!")


def resource_check(order):
    for ingredient in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
            print("Sorry there is not enough " + ingredient + ".")
            return
    process_order(order)


prompt = True
drink_number = 0
while prompt:
    user_drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_drink == "espresso":
        resource_check("espresso")
    elif user_drink == "latte":
        resource_check("latte")
    elif user_drink == "cappuccino":
        resource_check("cappuccino")
    elif user_drink == "off":
        prompt = False
    elif user_drink == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(bank["money"]))
    else:
        print("That is not a drink option.")
