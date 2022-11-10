"""
contextuxmanager: with utasítás

Mi az a contextusmanager: egy olyan megoldás a pythonban, hogy
a contexmanagernél használt erőforrást manageli.

"""


file_path = r"C:\WORK\2022_oktober_python\8. alkalom\Dracula.txt"

# best practicek
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()


print(data[0:500])