class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        # Returns the total calculated from coins inserted.
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

    def transaction_result(self, coins, cost):
        ##Return True when the payment is accepted, or False if money is insufficient.
        return coins >= cost

