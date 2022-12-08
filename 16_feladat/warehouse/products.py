"""
This module for represents product related classes
"""

class Product:
    def __init__(self, price, type="Other", subtype=None):
        self.price = price
        self.type = type
        self.subtype = subtype


if __name__ == '__main__':
    salami = Product(price=4500, type="Meat", subtype="salami")
    sausage = Product(price=3500, type="Meat", subtype="sausage")
    quark = Product(price=780, type="Milk", subtype="quark")
    pen = Product(price=400, type="Other")

    print(salami.price)