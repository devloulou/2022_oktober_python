"""
This module handles file related tasks
"""


# amikor a feladathoz csak az elvárt eredményt fejlesztem le -> "happy path" valósult meg
# use case - felhasználási esetek
# edge case - corner case: azok az esetek, kevés valószinűséggel előforduló esetek,
# viszont számítani kell rá
import os

def read_txt(file_path):
    """
    This function opens a .txt file and return it's value
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Given file {file_path} is not exists")

    with open(file_path, 'r', encoding="utf-8") as f:
        data = f.read()    
    
    return data

def write_json(file_path, json_data):
    import json

    if not os.path.exists(os.path.dirname(file_path)):
        raise FileNotFoundError(f"Given file {file_path} is not exists")

    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4) 
    
    return True


if __name__ == '__main__':
    file_path = r"C:\WORK\2022_oktober_python\9. feladat\Dracula.txt"
    json_path = r"C:\WORK\2022_oktober_python\9. feladat\statistics.json"
    data = read_txt(file_path)
    
    my_dict = {"kulcs": "érték"}
    write_json(json_path, my_dict)