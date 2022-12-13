"""
This module handle file related tasks
"""
import os

# elvárt működést első sorban lefejleszteni - happy path

# over engineering
class FileHandler:

    def __init__(self):
        self.__file_path = None

    @property #getter függvény
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, fpath):
        self.__file_path = fpath

    def get_data_from_txt(self):
        if not os.path.exists(self.__file_path):
            raise FileExistsError(f"The given file: {self.__file_path} is not exists")

        with open(self.__file_path, "r", encoding="utf-8") as f:
            data = f.read()

        return data

    # nem használ semmit az osztály attributumai közül
    # statikus függvény legyen - > @staticmethod
    # ő nem lát semmit sem az osztály attributumai közül -> nem is tudja azokat módosítani
    # attributum: az osztály tartozó függvények, változók
    # utility megoldást kell csinálni
    # statikus függvényhez nem szükséges az osztályt példányosítani
    @staticmethod
    def create_data_for_insert(txt_data):
        # [(a, b, c, d,....), (a, b, c, d, ....)]
        rows = data.split('\n')
        cols = rows.pop(0).split(',')

        # insert_data = []
        # for item in rows[1:]:
        #     insert_data.append(tuple(item.split(',')))
        insert_data = {
            "cols": cols,
            "data": [tuple(item.split(',')) for item in rows]
        }
        return insert_data


        

if __name__ == '__main__':
    test = FileHandler()

    test.file_path = r"C:\WORK\2022_oktober_python\17. alkalom\data\employee.txt"

    data = test.get_data_from_txt()

    ins_data = test.create_data_for_insert(data)

    print(ins_data)