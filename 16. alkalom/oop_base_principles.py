"""
Object Oriented Programming - OOP

osztályok definiálni
osztályoknak lesznek tulajdonságai, attributumai, függvényei stb.

osztályokból -> objektumokat fogunk létrehozni

"""

class MyClass:
    pass

"""
Abstraction - absztrakció: rejtsd el a kódot a használat helyétől
"""

class Human:
    """
    __init__ : az osztály konstruktora - construct
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
példányosítás
"""

a = 10
# print(type(a))

# joco = Human("Jocó", 45)
joco = Human(name="Jocó", age=45)
# print(joco.age, joco.name)

joco.age = 46

# print(joco.age)

"""
Vigyázat, az, hogy nem létezik egy instance változó az osztályban,
az nem jelenti azt, hogy nem tudok értéket adni neki
"""
joco.sex = "Man"

# print(joco.sex)

"""
Inheritencia - Inheritance - Öröklődés
szülő - gyermek kapcsolatot

örökölődés: az ős osztály attributumait, függvényeit örökölteti a gyermek felé,
és az öröklődés után tudjuk használni az ős osztályban deifiniált attributumokat, tulajdonságokat, függvényeket

A python képes arra, hogy egyszerre több ősosztálya legyen
"""
# ősosztály
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hello {self.name}")


# self: lehet kutyacica
# gyermek osztály
class Woman(Human):
    def __init__(self, name, age):
        self.sex = "woman"
        # Human.__init__(self, name, age)
        super().__init__(name, age)

    def say_hi(self):
        print("Ez egy nagyon szép nap, igaz?")

    # def say_hi(self):
    #     super().say_hi()

aranka = Woman(name="Aranka", age=70)

# print(aranka.name, aranka.age, aranka.sex)

aranka.say_hi()


##############################
"""
Polimorphism - többalakúság

"""

my_string = "Hello"
my_list = [1, 2, 3, 4]
my_tuple = (1, 2)
my_dict = {"key": 1}
my_set = {5,6,7,8,9,10}

# polimorh függvény a len
# print(len(my_string))
# print(len(my_list))
# print(len(my_tuple))
# print(len(my_dict))
# print(len(my_set))

"""
Encapsulation - egységbe zárás
Minden az objektumhoz tartozó metodus, változó, attributum legyen private
hacsak nem teszem publikussá őket

A pythonban nincs olyan, hogy private, nincs valódi láthatóság szabályozás
"""

class Test:
    def __init__(self):
        self.__price = 10_000
        self.__pin = 1234

    def __get_pin_code(self):
        return self.__pin

    def print_pint_code(self):
        print(self.__pin)

    def set_pin(self, val):
        self.__pin = val

test = Test()

# print(test.__pin)
# print(test.__get_pin_code())
test.set_pin(5678)
test.print_pint_code()

test._Test__pin = 9234
print(test._Test__pin)