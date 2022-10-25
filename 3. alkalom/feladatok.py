# 1. feladat:
# lista műveletekkel adjatok az alább megadott üres listához tetszőleges értékeket

my_list = []

my_list.append('testszőleges')
my_list.extend([1, 2, 3, 4, 5])
my_list.insert(1, "Karcsi")


#print(my_list)

# 2. feladat:
# az utolsó 2 értéket módosísátok tetszőleges értékre

my_list = ["Ricsi", "Géza", "Karcsi", "Peti"]

my_list[-2] = 'Pisti'
my_list[-1] = 'Feri'

my_list[-2:] = [1, 2]
# my_list[0:2] = [1, 2]

# print(my_list)

# 3. feladat:
# az alábbi dictionary-ben töröljük a zip_code értékét

my_dict = {
    "shop": {
        "shop_name": "Reál",
        "zip_code": "1111",
        "type": "general store"
    }
}

# my_dict['shop'].pop('zip_code')
del my_dict['shop']['zip_code']

# print(my_dict)

# 4. feladat:
# írjatok olyan if else kódblockot
# amely, ha a num1 > num2 -> eredmény = num1/num2
# ha num2 > num1 -> eredmény = num1 + 10

num1 = 10
num2 = 20

solution = 0

if num1 > num2:
    solution = num1/num2
elif num2 > num1:
    solution = num1 + 10

# print(solution)

# 5. feladat:
# írjatok egy olyan kódot, amely minden elemnek veszi az 1/10 részét:.
# elvárt eredmény: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

temp = []
for item in my_list:
   temp.append(int(item/10))

print(temp)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list = [int(item/10) for item in my_list]

print(my_list)