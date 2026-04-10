class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(p.price for p in self.items)

cart = Cart()
cart.add(Product("Laptop", 50000))
cart.add(Product("Mouse", 500))

print("Total:", cart.total())