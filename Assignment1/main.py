resources = {
    "bread": 12,  # slices
    "ham": 18,  # slices
    "cheese": 24  # ounces
}
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slices
            "ham": 4,  # slices
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slices
            "ham": 6,  # slices
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slices
            "ham": 8,  # slices
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

# Helper functions
def check_resources(size):
    recipe = recipes[size]
    ingredients = recipe["ingredients"]
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            return f"Sorry, there is not enough {ingredient}."
    return True

def process_coins():
    coin_types = {
        "large dollar": 1,
        "half dollar": 0.5,
        "quarter": 0.25,
        "nickel": 0.05
    }
    coin_amounts = {}
    total_cost = 0
    for coin, value in coin_types.items():
        coin_amounts[coin] = int(input(f"How many {coin}s?: "))
        total_cost += coin_amounts[coin] * value
    return total_cost, coin_amounts

def make_sandwich(size):
    recipe = recipes[size]
    ingredients = recipe["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    return f"{size} sandwich is ready. Bon appetit!"

def show_report():
    for ingredient, amount in resources.items():
        print(f"{ingredient.capitalize()}: {amount} slice(s)")

# Main function
def run_machine():
    while True:
        order = input("What would you like? (small/ medium/ large/ off/ report): ")
        if order == "off":
            print("Turning off the machine.")
            break
        elif order == "report":
            show_report()
        elif order in recipes:
            check = check_resources(order)
            if check != True:
                print(check)
            else:
                print("Please insert coins.")
                total_cost, coin_amounts = process_coins()
                if total_cost < recipe[order]["cost"]:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    change = total_cost - recipe[order]["cost"]
                    print(f"Here is ${change} in change.")
                    print(make_sandwich(order))
        else:
            print("Invalid option.")


