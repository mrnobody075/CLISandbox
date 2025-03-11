rsour = {
    'Water':300,
    'Milk':200,
    'Coffee':100,
    'Money':0

}

EachDrink = {
    'espresso':{
        'Water':50,
        'Milk':0,
        'Coffee':18,
        'Cost':1.5
    },
    'latte':{
        'Water':200,
        'Milk':150,
        'Coffee':24,
        'Cost':2.5
    },
    'cappuccino':{
        'Water':250,
        'Milk':100,
        'Coffee':24,
        'Cost':3.0
    }
}
coins = {
    'penny':0.01,
    'dime':0.1,
    'nickel':0.05,
    'quarter':0.25
}
insertedCoins = {
    'penny':0,
    'dime':0,
    'nickel':0,
    'quarter':0
}
machineSwitch = True
money = rsour['Money']
def askCustom():
    print("What would you like? (espresso/latte/cappuccino):")
def checkIfOff():
    global machineSwitch
    machineSwitch = False
    print(rsour['Money'])
def report():
    print(f"The current resources are:")
    for i in rsour:
        if i == 'Money':
            print(f"{i}: ${rsour[i]}")
        else:
            print(f"{i}: {rsour[i]}ml")
def prepareDrink(ingredients):
    global rsour
    rsour['Water'] -= ingredients['Water']
    rsour['Milk'] -= ingredients['Milk']
    rsour['Coffee'] -= ingredients['Coffee']
def refill():
    global rsour
    rsour['Water'] = 300
    rsour['Milk'] = 200
    rsour['Coffee'] = 100

while(machineSwitch):
    askCustom()
    typeOfDrink=str(input()).lower()

    match typeOfDrink:
        case 'report':
            report()
        case 'off':
             checkIfOff()
        case 'espresso':
            print(f"The price is ${EachDrink['espresso']['Cost']}, checking if it can be prepared")
        case 'cappuccino':
            print(f"The price is ${EachDrink['cappuccino']['Cost']}, checking if it can be prepared")
        case 'latte':
            print(f"The price is ${EachDrink['latte']['Cost']}, checking if it can be prepared")
        case 'refill':
            refill()
        case 'collection':
            print(rsour['Money'])
        case _:
            print("Sorry, we don't have that yet")
    cont = True
    ingredients={}
    try:
        ingredients = EachDrink[typeOfDrink]
        for item, ingredient in ingredients.items():
            if item != 'Cost' and rsour[item] < ingredient:
                print(f"Sorry,{item} is not enough. Ask the barista to refill the machine")
                cont = False
        if cont == True and cont == True:
            print("Accepted coins are: ")
            for i in coins:
                print(f"{i}")
        try:
            while ingredients['Cost'] > money and cont == True:
                print("Insert coins: ")
                for i in insertedCoins:
                    insertedCoins[i] = int(input(f"Enter number of {i}s: "))
                for i in insertedCoins:
                    if i == 'penny':
                        money += insertedCoins[i] * 0.01
                    elif i == 'dime':
                        money += insertedCoins[i] * 0.1
                    elif i == 'nickel':
                        money += insertedCoins[i] * 0.05
                    elif i == 'quarter':
                        money += insertedCoins[i] * 0.25
                print(f"Total inserted: ${money:.2f}")
                if money < ingredients["Cost"]:
                    print(f"Not enough money! You need ${ingredients['Cost'] - money:.2f} more.")
                    print("Insert more coins...\n")
                if ingredients['Cost'] < money:
                    change = money - ingredients['Cost']
                    money -= change
                    print(f"Here's your change:${change}")
        except ValueError:
            print("Coin Not accepted, Please try again")
            continue

        if cont:
            print("Your drink is being prepared please wait...")
            print('1')
            print('2')
            print('3')
            prepareDrink(ingredients)
            print("Ready! please take ur drink and enjoy")

        rsour['Money'] += money
        money = 0
    except KeyError:
        print("----")




