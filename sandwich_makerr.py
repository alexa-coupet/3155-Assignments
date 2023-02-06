from Data import recipes

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient) is None:
                return False
            if self.machine_resources[ingredient] < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(recipes[sandwich_size]["ingredients"]):
            for ingredient, amount in recipes[sandwich_size]["ingredients"].items():
                self.machine_resources[ingredient] -= amount
            return True
        return False
