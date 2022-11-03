# modulok a pythonban
# modul: minden .py kiterjesztéső file egyben modul is
# a package: modulok mappába szervezve - ennek van egy strukturális követelménye

# minden modulfile, amikor a __name__ változó értékét lekérjük magában a file-ban, akkor
# a __main__ nevet kapja

# amikor bárhová beimportáljuk a modult, akkor a __name__ változó
# a file valódi nevét fogja értékül kapni

# import test_file
from test_file import my_list

