# függvények - functions
# függvények használatával elkerültehő a kód ismétlés - kód redundancia
# a már lefejlesztett függvény bármikor, bármennyiszer újra meghívható

"""
def function_name(paraméterek:opcionális):
    itt a kód rész
"""
# user defines function - felhasználó által létrehozott függvény
# paraméter nélküli függvénymegadás
def hello():
    print("Hi")

# beépített python függvény
# print("szia") # ez egy függvényhívás
# hello() # függvényhívás

# print()


# függvény paraméterekkel
def fnc_summa(a, b):
    print(a+b)

# fnc_summa(2,3)

# függvény paraméterrel, de kezdőértékkel: default 
def fnc_summa(num1=10, num2=12):
    print(num1)
    # print(num1 + num2)

# fnc_summa(2,7)   
# fnc_summa(2)   
# fnc_summa()

# fnc_summa(num1=11, num2=120)
# fnc_summa(num2=110, num1=150)

# packing és unpacking: 

# *args - **kwargs
def fnc_test(*args):
    print(args)

# fnc_test(1, 2, 4, 5, 6, 7, "Ricsi", print, [1,2, "Dani"])

# fnc_test()

def fnc_kwargs(**kwargs):
    print(kwargs)

# fnc_kwargs(auto="BWM", price=1_500_000, color="yellow")

def fnc_args_kwargs(*args, **kwargs):
    print(args)
    print("------------------")
    print(kwargs)



# fnc_args_kwargs(1, 2, 3, "Ricsi", "Peti elemnet játszani", (1, 4, 5), auto="Volvo", color="black")
# fnc_args_kwargs(1, 2, 3, "Ricsi",  "Peti elemnet játszani", (1, 4, 5), price=2_000_000, auto="Volvo", color="black")


# a függvénynek minden esetben van visszatérési értéke

# fnc_test("Ricsi", "Peti", "Karcsi")

# None - semmi, null
#visszatérési érték : return szó utáni kifejezés
# a visszatérési értéket "el lehet menteni változóba"

def fnc_test():
    return "Ricsi"

my_val = fnc_test()

# print(my_val)

# függvények vezérlése
# a return megállítja a fügvény futását, befejezi azt

def fnc_test():
    # print("KEzdődik")
    return
    

my_val = fnc_test()

# print(my_val)


def add_numbers(num1, num2):
    return num1 + num2

solution = add_numbers(10, 30)

# print(solution)


# visszatérünk a lista, dictionary dolgokhoz
# megnézzük, hogy mi az hogy modul, package
# file műveletek alapjait

def add_numbers(*args):
    solution = 0
    for item in args:
        solution += item
        # solution = solution + item

    return solution


temp = add_numbers(1, 2, 1, 200, 3, 1, 2,333 , 4, 544, 6, 155,3)

print(temp)