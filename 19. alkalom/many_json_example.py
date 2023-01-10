# Thread - a python NEM KÉPES VALÓJÁBAN A THREAD HASZNÁLATRA
# pythonban is létezik a Thread -> amiatt nem tud a pythonban megvalósulni, mert a threadnek
# egy nagyon fontos követelménye van: a szálak között legyen megosztott memória

# a python nem képes erre -> GIL -> Global Interpreter Lock -> a futó programot egy elszeparált Heap
# típusú memóriában "elzárja a külvilágtól"

# multiprocessing -> több futó 
####################################################################################
# meg kellene vizsgálni ezeket a file-okat
# megnézni, hogy milyen kulcsaik vannak
# van e eltérés a kulcsok között

# legerősebb autó
# leggyengébb
# legöregebb
# legfiatalabb

# json-be írjuk ki a statisztikát

# 1. a mappa tartalmát - a file-ok neveit - felolvassuk egy listába
# 2. meg kell nyitnunk a file-okat olvasásra, egyesével

# kell egy olyan függvény, ami megnyitja a file-okat és visszaadja a tartalmát
# kell egy olyan függvény, ami a mappa tartalmát visszaadja egy listába 
# -> teljes elérési útvonal


import os
import json

# a python unicode
def get_files_from_folder(folder_path):
    return [os.path.join(folder_path, item) for item in os.listdir(folder_path)]

def get_data_from_json(json_path):
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Given file {json_path} is not exists")
    
    with open(json_path, "r", encoding="utf-8") as obj:
        data = json.load(obj)

    return data


if __name__ == '__main__':
    folder_path = r"C:\WORK\2022_oktober_python\19. alkalom\4_jsons"
    files = get_files_from_folder(folder_path)

    first_keys = []
    temp = []
    mkeys = []
    for idx, item in enumerate(files):
        data = get_data_from_json(item)
        mkeys = []

        if idx == 0:
            first_keys = list(data.keys())

        for key in data.keys():
            if key not in first_keys:
                mkeys.append(key)
            
        if mkeys:
            temp.append({
                "file_path": item,
                "keys": mkeys
            })

        # if idx == 1:
        #     print(temp)
        #     break
    print(temp)