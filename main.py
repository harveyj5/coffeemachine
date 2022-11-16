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
#TODO: 5. Check resources sufficient to make drink order
def report():
    print(resources)
#TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
order = input("What would you like? (espresso/latte/cappuccino): ").lower()
if order == [f'{order}']:
    print(f"Your order is not valid.")
    exit()
#TODO: 4. Print a report of the coffee machine resources
elif order == "report":
    report()
    exit()
# TODO: 3. Turn off the coffee Machine by entering "off" to the prompt."
elif order == "off":
    print("The coffee machine is now turning off.")
    exit()

#TODO: 2. Check the user's input to decide what to do next.
cost = MENU[f'{order}']['cost']
if MENU[f'{order}']['ingredients']['water'] <= resources['water'] and MENU[f'{order}']['ingredients']['coffee']<=resources['coffee']:
    print(f"Your {order} is brewing.")
    resources['water']= resources['water']-MENU[f'{order}']['ingredients']['water']
    resources['coffee'] = resources['coffee']-MENU[f'{order}']['ingredients']['coffee']
    print(resources)

    print(cost)
elif MENU[f'{order}']['ingredients']['water'] <= resources['water'] and MENU[f'{order}']['ingredients']['milk']<=resources['milk'] and MENU['order']['ingredients']['coffee'] <= resources['coffee']:
    print(f"Your {order} is brewing.")
    resources['water'] = resources['water'] - MENU[f'{order}']['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[f'order']['ingredients']['coffee']
    resources['milk'] = resources['milk'] - MENU[f'{order}']['ingredients']['milk']
    print(resources)
    print(cost)

else:
    print("Sorry there is not enough resources for your order")




#TODO: 6. Process Coins
#TODO: 7. Check transaction successful




