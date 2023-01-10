
class TestClass:
    def __init__(self):
        pass

#attributum: függvények, változók összessége
class Auto:
    price = 10_000 # osztályhoz tartozik
    def __init__(self, brand, motor_type, color):
        self.brand = brand
        self.motor_type = motor_type
        self.color = color

    def print_color(self):
        print(self.color)

bmw = Auto(brand="BMW", motor_type="benzin", color="black") # példányosítás -> instance

mercedes = Auto(brand="Mercedes", motor_type="benzin", color="black")


# print(bmw.brand)
# print(mercedes.brand)

# print(bmw.price)
# print(mercedes.price)

# print(Auto.price)

# Auto.price = 50_000

# print(bmw.price)
# print(mercedes.price)

# private változó -> a pythonban a private szabályozás nem valódi private szabályozás
# publikus - bárki láthatja
# getter - setter - deleter metódusok
class TestClass:
    def __init__(self):
        self.__my_age = 110
        self.age = 40

    @property
    def my_age(self):
        pass

    @my_age.getter # getter függvény
    def my_age(self):
        return self.__my_age

    @my_age.setter
    def my_age(self, value):
        self.__my_age = value

    @my_age.deleter
    def my_age(self):
        del self.__my_age

    def kiir(self):
        print(self.__my_age)


test = TestClass()
test.my_age = 160

print(test.my_age)


del test.my_age


# print(test._TestClass__my_age) #> ez a bizonyíték, hogy a private a pythonban nem valódi private mechanizmus

# test._TestClass__my_age = 130

