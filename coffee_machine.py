class CoffeeMachine:
    coffee_machine_stock = {
        "water": 400,
        "milk": 540,
        "beans": 120,
        "cups": 9,
        "money": 550
    }

    products = {
        "espresso": {"water": 250, "beans": 16, "cups": 1, "money": 4},
        "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7},
        "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}
    }
    options = {
        "1": "espresso",
        "2": "latte",
        "3": "cappuccino"
    }

    def display_supplies(self):
        print("\nThe coffee machine has:")
        print(self.coffee_machine_stock["water"], " ml of water")
        print(self.coffee_machine_stock["milk"], " ml of milk")
        print(self.coffee_machine_stock["beans"], " g of coffee beans")
        print(self.coffee_machine_stock["cups"], " disposable cups")
        print("$", self.coffee_machine_stock["money"], " of money\n")

    def add_supplies(self, water: int, milk: int, beans: int, disposable_cups: int):
        self.coffee_machine_stock["water"] += water
        self.coffee_machine_stock["milk"] += milk
        self.coffee_machine_stock["beans"] += beans
        self.coffee_machine_stock["cups"] += disposable_cups

    @staticmethod
    def missing_ingredient_alert(item):
        print(f"Sorry, not enough {item}")

    def check_stock(self):
        for product, ingredients in self.products.items():
            for ingredient, amount in ingredients.items():
                if ingredient != "money" and amount > self.coffee_machine_stock[ingredient]:
                    self.missing_ingredient_alert(ingredient)
                    return False
                else:
                    return True

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        if choice == "back":
            return
        elif self.check_stock():
            print("I have enough resources, making you a coffee!")
            self.coffee_machine_stock["water"] -= self.products[self.options[choice]].get("water")
            self.coffee_machine_stock["milk"] -= self.products[self.options[choice]].get("milk", 0)
            self.coffee_machine_stock["beans"] -= self.products[self.options[choice]].get("beans")
            self.coffee_machine_stock["cups"] -= self.products[self.options[choice]].get("cups")
            self.coffee_machine_stock["money"] += self.products[self.options[choice]].get("money")

    def fill(self):
        print("Write how many ml of water you want to add: ")
        water_to_add = int(input())
        print("Write how many ml of milk you want to add: ")
        milk_to_add = int(input())
        print("Write how many grams of coffee beans you want to add: ")
        beans_to_add = int(input())
        print("Write how many disposable cups you want to add: ")
        cups_to_add = int(input())
        self.add_supplies(water_to_add, milk_to_add, beans_to_add, cups_to_add)

    def take(self):
        print(f"\nI gave you $", self.coffee_machine_stock["money"])
        self.coffee_machine_stock["money"] -= self.coffee_machine_stock["money"]

    def start(self):
        while True:
            print("Write action (buy, fill, take): ")
            action = input()
            if action == "remaining":
                self.display_supplies()
            elif action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "exit":
                exit()


def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.start()


if __name__ == "__main__":
    main()
