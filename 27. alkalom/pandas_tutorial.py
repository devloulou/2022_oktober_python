"""
Pandas: data library - data modul

3 object típus:
Series: mint egy oszlop az excelben
DataFrame: mint egy adatbázis tábla
Panel - nem fogjuk kivesézni -> multi dimenzionális "tömb"


"""

import pandas as pd
import numpy as np
"""
[[1, 2,3], [4, 5, 6]]

pl.
pd.Series(data, index, dtype, copy)

data maga az adat: ndarray, list, constans
index: az értéke unique és hashalhetőnek kell lennie -> int , float , str , tuple , and NoneType
dtype: meg tudjuk adni az addtípust, ha nem adjuk meg, akkor "kitatlálja"

dtype == 'object' -> string
"""

my_list = [item for item in range(100, 105)]

s = pd.Series(my_list, index=['a', 'b', 'c', 'd', 'e'])

s.index = ['Ricsi', "Karcsi", 'Peti', 'Laci', 'Pisti']

# print(s[::2])

# print(s[['Ricsi', "Pisti"]])
# print(s.index)


my_dict = {"day1": 420, "day2": None, "day3": 390}

s = pd.Series(my_dict)

# print(s)
# print("----------------")
s.fillna(s.median(), inplace=True)

# print(s)
# print(s.fillna())
# print(s.index)

# print(dir(s))


"""
DataFrame

Mint egy adatbázis táblát, úgy képzeljük el

pandas.DataFrame(data, index, columns, dtype, copy)

Series-ekből áll
"""

data = {
    "calories": [430, 530, 1230],
    "duration": [120, 200, 400]
}

df = pd.DataFrame(data)

# print(df.head(1))

# print(df.columns)
# print(df.dtypes)

# print(df[['calories', 'duration']])

df['calories'] = df['calories'].astype('float', errors='ignore')
# print(df.dtypes)

file_path = r"C:\WORK\2022_oktober_python\17. alkalom\data\employee.txt"

df = pd.read_csv(file_path, sep=',')

df.replace({np.nan: None}, inplace=True)

print(df.head(4))

df = df.to_dict(orient="records")

import json

with open("pandas_test.json", "w", encoding="utf-8") as f:
    json.dump(df, f, indent=4)

print(df)

