# Solo code 7
class Groceryshop:
    def __init__(self, cost, quantity):
        self.cost = cost
        self.quantity = quantity

        # Make private class of groceries between vegies and fruits
class Vegies(Groceryshop):
    def __init__(self, cost, quantity):
        super().__init__(cost, quantity)

class Fruits(Groceryshop):
    def __init__(self, cost, quantity):
        super().__init__(cost, quantity)

        # Have fruit and vegies be priced differently
    def price(self):
        if isinstance(self, Vegies):
            return self.cost * self.quantity * 0.8
        elif isinstance(self, Fruits):
            return self.cost * self.quantity * 1.2

            # Print the total cost of fruits if the cost of vegies is 10 and quantity is 3, and the cost of fruits is 15 and quantity is 8
vegies = Vegies(10, 3)
fruits = Fruits(15, 8)

print("Total cost of veggies:", vegies.price())
print("Total cost of fruits:", fruits.price())