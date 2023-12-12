# addint inputs to a variable
'''
coins_inserted = 0
coins_inserted += int(input("Add Quarters: ")) * .25
coins_inserted += int(input("Add Dimes: ")) * .1
coins_inserted += int(input("Add Nickels: ")) * .05
coins_inserted += int(input("Add Pennies: ")) * .01
print(f"${coins_inserted}")
'''
# compare two dictionaries where one is deeply nested

MENU = {
    "espresso": {
        "ingredients": {
            "water": 200,
            "coffee": 100,
        }
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "coffee": 100,
            "milk": 50
        }
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "coffee": 100,
            "milk": 100
        }
    }
}

resources = {
    "water": 10,
    "coffee": 10,
    "milk": 100
}

coffee = input("espresso/latte/cappuccino: ")
coffee_choice = MENU[coffee]

def order_coffee():
    for item in coffee_choice["ingredients"]:
        if coffee_choice["ingredients"][item] > resources[item]:
            return False
        else:
            return True

print(order_coffee())