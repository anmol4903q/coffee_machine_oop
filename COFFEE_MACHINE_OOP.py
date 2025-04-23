# ☕ Coffee Class - Blueprint for each type of coffee
class coffee:
    def __init__(self, name, cost, milk, water, coffee):
        self.name = name
        self.cost = cost
        # 🧪 Recipe for the coffee
        self.recipe = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

# 🛠️ CoffeeMachine Class - Handles everything: menu, ingredients, orders, payments
class CoffeeMachine:
    def __init__(self):
        # 📦 Initial available ingredients
        self.ingredients = {
            "water": 1000,
            "milk": 800,
            "coffee": 500
        }

        # 📜 Coffee Menu
        self.menu = [
            coffee("espresso", 100, 50, 0, 18),
            coffee("latte", 150, 200, 150, 24),
            coffee("cappuccino", 170, 250, 100, 24)
        ]

    # 📋 Display the menu to the user
    def display_menu(self):
        print("📋 Available Coffees:")
        for i in self.menu:
            print(f"➡️ {i.name.capitalize()} : ₹{i.cost}")

    # ✅ Check if there are enough ingredients for selected coffee
    def check_ingredients(self, coffee):
        for i in coffee.recipe:
            if coffee.recipe[i] > self.ingredients[i]:
                print(f"❌ Not enough {i}.")
                return False
        return True

    # 💰 Handle payment from the user
    def process_payment(self, coffee):
        total = 0
        while True:
            r = input("💵 Enter rupees (type 'done' when you're finished): ")
            if r.lower() == "done":
                break
            if r.isdigit():
                total += int(r)
                print(f"✅ You have inserted ₹{total}")
            else:
                print("⚠️ Please enter a valid number or type 'done'")

        if total >= coffee.cost:
            change = total - coffee.cost
            if change > 0:
                print(f"💸 Your change: ₹{change}")
            print("☕ Enjoy your coffee!")
            return True
        else:
            print("❌ Not enough money! Refunding...")
            return False

    # 📦 Handle order process
    def take_order(self):
        order = input("🛎️ What would you like to order? ").lower()
        if not order:
            print("❌ Invalid choice.")
            return

        choosed = None
        for i in self.menu:
            if i.name == order:
                choosed = i
                break

        if choosed is None:
            print("❌ Coffee not found on menu.")
            return

        if not self.check_ingredients(choosed):
            return

        if not self.process_payment(choosed):
            return

        self.make_coffee(choosed)

    # 🧑‍🍳 Make the coffee and reduce ingredients
    def make_coffee(self, coffee):
        for i in coffee.recipe:
            self.ingredients[i] -= coffee.recipe[i]
        print("✅ Your coffee is ready! ☕")

# 🚀 Run the Coffee Machine
machine = CoffeeMachine()
machine.display_menu()
machine.take_order()
