import Data
from sandwich_makerr import SandwichMaker
from cashier import Cashier

# Create two variables based on data dictionaries (resources and recipes)
resources = Data.resources
recipes = Data.recipes

# Create instances from each class
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    sandwich_type = input("What size sandwich do you want to order? (small, medium, large): ")
    cost = recipes[sandwich_type]["cost"]
    print("Cost of the sandwich:", cost)
    coins = cashier_instance.process_coins()
    if cashier_instance.transaction_result(coins, cost):
        if sandwich_maker_instance.make_sandwich(sandwich_type, recipes[sandwich_type]["ingredients"]):
            print("Your sandwich is being made!")
        else:
            print("We don't have the ingredients to make that sandwich.")
    else:
        print("Insufficient funds. Please insert more coins.")


if __name__ == "__main__":
    main()

