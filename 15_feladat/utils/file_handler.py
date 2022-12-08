import os
import json

def get_data_from_txt(txt_path):
    if not os.path.exists(txt_path):
        raise FileNotFoundError(f"Given path: {txt_path} not exists")
    
    with open(txt_path, "r", encoding="utf-8") as f:
        data = f.read()

    return data


def write_json(json_path, data):
    if not os.path.exists(os.path.dirname(json_path)):
        raise FileNotFoundError(f"Given folder: {os.path.dirname(json_path)} not exists")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    temp = []
    folder_path = r"C:\WORK\2022_oktober_python\15_feladat\books"
    for item in os.listdir(folder_path):
        if item.endswith(".txt"):
            txt_path = os.path.join(folder_path, item)
            temp.append(txt_path)

    files = [os.path.join(folder_path, item) for item in os.listdir(folder_path) if item.endswith(".txt")]

    for item in files[0:1]:
        print(item)
        data = get_data_from_txt(item)

        json_path = item.replace("txt", "json")
        # itt fogom a statisztikákat előállítani
        data = {}
        write_json(json_path, data)
