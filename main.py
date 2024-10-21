from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
cf = CoffeeMaker()
menu = Menu()


turn_off = False
while not turn_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "report":
        cf.report()
        mm.report()
    elif choice == "off":
        print("Coffee machine is turned off")
        turn_off = True
    else:
        drink = menu.find_drink(choice)
        if cf.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cf.make_coffee(drink)
