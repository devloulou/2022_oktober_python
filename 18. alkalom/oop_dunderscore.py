"""
függvény név: __funcname__ típusú függvényeket magic methodnak,
            dunderscore methodnak - double underscore-t

ezek speciális függvények

"""

class Test:
    def __init__(self, name="Ricsi"):
        self.name = name

    def __str__(self):
        return f"ez egy test object a {self.__class__} osztályból"

    def __len__(self):
        return len(self.__str__())

    def __del__(self):
        print("Törlés elindult")


test = Test()

test.__str__()

del test


print(len(test))