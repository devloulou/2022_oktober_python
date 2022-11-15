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