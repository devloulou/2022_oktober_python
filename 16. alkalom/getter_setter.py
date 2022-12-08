"""
'private' attributumok kezelésére getter, setter, deleter metódusokat célszerű használni

2 féle megközeletíse van az osztályok létrehozásának
 - behavioural - viselkedést  - eseményeket
 - data - adatot akarod

"""
# 1. publikus fügvényekkel lekérni, módosítani, törölni az attributumot
class TestClass:
    def __init__(self):
        self.__value = 0

    # "setter" függvény
    def set_value(self, val):
        self.__value = val
    
    # "getter" függvény
    def get_value(self):
        return self.__value

    # "deleter" függvény
    def del_value(self):
        del self.__value

test = TestClass()

# print(test.get_value())
# test.set_value(10)
# print(test.get_value())

# test.del_value()

# test._Test__name = "Ricsi"
# # print(test.__name)
# print(test._Test__name)

# 2. propery() használata

class TestClass:
    def __init__(self):
        self.__value = 100_000

     # "setter" függvény
    def __set_value(self, val):
        self.__value = val
    
    # "getter" függvény
    def __get_value(self):
        return self.__value

    # "deleter" függvény
    def __del_value(self):
        del self.__value

    value = property(__get_value, __set_value, __del_value)

test = TestClass()


# print(test.value)
# test.value = 10_00
# print(test.value)

# del test.value

# print(test.value)

# 3. @property - property decorator

class TestClass:
    def __init__(self):
        self.__value = 100_000

    @property # getter metódus
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @value.deleter
    def value(self):
        del self.__value


test = TestClass()

test.value = 100

print(test.value)

del test.value

print(test.value)