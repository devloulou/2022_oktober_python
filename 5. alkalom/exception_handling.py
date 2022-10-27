
my_list = ["Ricsi", "Kati", "Gizi", "Piri", "5"]

# isinstance

# print(isinstance("Ricsi", int))

# print(isinstance("5", int))

# print(type(my_list))

# kivétel kezelés
"""
try:
    valamilyen műveletek
except:
    itt kezeljük le a hibát
(opcionális)
finally:
    ez minden esetben le fog futni

"""
# próbáljuk meg számmá alakítani a my_val változót
# azt a műveletet, amikor egy adott adattípust egy más adattípussá akarunk átalakítani
# típus konverziónak, típus castolásnak nevezzük

# try: except közötti rész, ha lefut hiba nélkül, akkor nem volt kivétel -> nem volt hiba
# ha hiba történik a try: except között, akkor az except ágra ugrik a futás és 
# az exceptnél megadott műveletek fognak lefutni

# finally ág: függetlenül attól, hogy volt e hiba, vagy nem volt, ez mindig lefut
# a finally opcionális, nem kötelező

# my_val = "5a"

# try:
#     int(my_val)
#     print("sikerült")
# except Exception as error:
#     print(error)
# finally:
#     print("ez mindig le fog futni")

# print(" sikeresen lekezeltem a hibát")

num1 = 2
num2 = 1

try:
    print(num1/num2)
    print(5+"Ricsi")
except ValueError as err:
    print("Érték hiba van")
except ZeroDivisionError as e:
    print("Nullával akartál osztani, ami nem lehetséges")
except Exception as error:
    print(error)
finally:
    print(" ez mindig lefut")

print("------------------------------------------")
my_list = ["Ricsi", "123", "Kati", "Gizi", "Piri", "5"]

for item in my_list:
    try:
        my_val = int(item)
    except Exception as e:
        continue

    print(my_val)
    print(type(my_val))