# json
# open fogjuk megnyitni a JSON file-unkat
# mivel a megnyitott file egy string, ezért nekünk át kell alakítani -> deserializáció nevezzük
# JSON filet megnyitjuk, felolvassuk belőle string-ként az adatot és python objektummá alakítjuk -> dictionary

# kiírás: létrehozok egy dictinary-t, azt ahogy akarom adattal populálom -> kiírom a dictionary-t JSON file -> serializáció

import json

# 4 db függvényt fogunk használni: load, loads -> file megnyitáshoz
#                                   dump, dumps -> file kiíráshoz

my_dict = {"kulcs": "érték"} # ez egy valid JSON is lehet
my_dict = {'kulcs': 'érték'} # ez nem lehet valid az aposztróf miatt

with open(r"C:\WORK\2022_oktober_python\9. alkalom\test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

my_dict = {"auto": "BMW", "color": "Blue"}

with open(r"C:\WORK\2022_oktober_python\9. alkalom\test2.json", "w", encoding="utf-8") as file:
    data = json.dump(my_dict, file)


my_json_string = json.dumps(my_dict)

print(my_json_string)

with open(r"C:\WORK\2022_oktober_python\9. alkalom\test3.json", "w", encoding="utf-8") as file:
    data = json.dump(my_json_string, file)

with open(r"C:\WORK\2022_oktober_python\9. alkalom\test3.json", "r", encoding="utf-8") as file:
    data = json.loads(json.load(file))

print(type(data))

data['kulcsocska'] = 12

print(data)

data = json.loads(my_json_string)

print(type(data))