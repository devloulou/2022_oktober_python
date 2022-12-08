from products import Product

class WareHouse:
    def __init__(self):
        self.products = {}

    # type hint - típus hint: a hint nem befolyásol semmilyen működést
    def store_product(self, cnt: int, product: Product) -> None:
        """
            letároljuk az objekteket, meg a darabszámot
            megoldandó: volt e már a megadott terméből
        """
        if self.products.get(product.subtype):
            "ha már létezik a termék az inventoryban"

        else:
            " ha nem létezik még a megadott termék"
            self.products[product.subtype] = {"cnt": cnt, "product": product}

    def pick_product(self):
        pass


if __name__ == '__main__':
    wh = WareHouse()
    salami = Product(price=4500, type="Meat", subtype="salami")
    sausage = Product(price=3500, type="Meat", subtype="sausage")
    quark = Product(price=780, type="Milk", subtype="quark")
    pen = Product(price=400, type="Other")

    wh.store_product(10, salami)


"""
következő alkalom:

befejezzük ezt a feladatot ~ 30 perc

virtualenv kialakítás
SQLAlchemy használatát
###################################################
ezután projekt munka:

Projekt munka:
filmekhez meta adat letöltő alkalmazást 
internetről fogunk borítóképet és különböző adatokat letölteni és letérolni adatbázisba

prostgres
MongoDB


Dockert: az adatbázis is dockerben fogjuk futtatni
a kódunkat is

Megtanuljuk a git kezelést

"""