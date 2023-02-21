import os
import pandas as pd

class FileHandler:
    def __init__(self):
        self.data_folder_path = None

    @staticmethod
    def get_data_from_csv(csv_path):
        return pd.read_csv(csv_path)

    def get_files_list(self):
        return [os.path.join(self.data_folder_path, item) \
                for item in os.listdir(self.data_folder_path)]

if __name__ == '__main__':
    from config import data_folder_path
    test = FileHandler()

    test.data_folder_path = data_folder_path

    files = test.get_files_list()

    for item in files[:1]:
        data = test.get_data_from_csv(item)

        print(data.dtypes)