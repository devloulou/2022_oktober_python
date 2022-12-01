""" A feladat:
Dracula.txt file-ról készítünk statisztikát
statisztikák:
    leghosszab sor
    állapítsuk meg, hogy hány oldala van: 3000 karakter ~ 1 oldal
    legrövidebb sor
    leggyakrabban előforduló 5 szó: szónak tekintem azt, ami legalább 5 karakter hosszú

Amikor a statisztikák elkészültek, írjuk ki az eredményt egy JSON file-ba, aminek legyen a neve:
statistics.json
"""

"""
A megoldáshoz vezető út:

1. meg kell nyitni  a Dracula txt: read_txt()
2. Statisztikák kidolgozása: visszaadom a függvények eredményét és letárolom egy dictionary-be
    - leghosszabb és a legrövidebbb, az lehetne 1 fv
    - állapítsuk meg, hogy hány oldala van: 3000 karakter ~ 1 oldal - az egészet 1 stringe
    - leggyakrabban előforduló 5 szó: szónak tekintem azt, ami legalább 5 karakter hosszú
3. kiírni a statisztikát

"""

from utils.file_handler import read_txt

def get_only_txt_file():
    import os
    folder_path = os.path.dirname(__file__)
    temp = []
    for item in os.listdir(folder_path):
        # if '.txt' in item:
        # if item.endswith('.txt'):
        if item[-4:] == '.txt':
            temp.append(item)
    print(temp)
    return [item for item in os.listdir(folder_path) if item.endswith('.txt')]


if __name__ == "__main__":
    files = get_only_txt_file()

    print(files)