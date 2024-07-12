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

def report():
    print(f"Water:{resources['water']}ml")
    print(f"Milk:{resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}g")
    print(f"Money: ${profit}")

def is_enough(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry that's not enough {item}.")
            return False
        else:
            return True    

def process_coins():
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) #çeyreklik
        dimes = int(input("How many dimes?: "))  #10 cent
        nickles = int(input("How many nickles?: ")) #5 cent
        pennies = int(input("How many pennies?: ")) #kuruş

        total = float(quarters*(0.25) + dimes*(0.1) + nickles*(0.05) + pennies*(0.01))
        return total



def is_transaction_succesful(money_received, drink_cost):
    """Return True when the payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingeridents):
    for item in order_ingeridents:
        resources[item] -= order_ingeridents[item]
    print(f"Here is your {drink_name}. Enjoy!")    


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)?: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    else:        
        drink = MENU[choice]
        if is_enough(drink["ingredients"]):
            given_money = process_coins()
            if is_transaction_succesful(given_money,drink['cost']):
                make_coffee(choice,drink["ingredients"])




