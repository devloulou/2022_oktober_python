#set: duplikáció mentes, iterálható objektum

my_set = set()
my_set = {1, 2, 3, 4, "Ricsi", "Ricsi"}

# print(type(my_set))

# print(my_set)

# {'Jolán' : [1, 4, 5, 6],
#             'Ibolya' : [1, 8, 9],
#             'Jácint': [10, 22, 4],
#             'Karcsi': [5, 11, 22],
#             # 'Pista': [8, 1, 4, 40]
#             }

my_set = {1, 4, 5, 6}
my_set = {8, 9}
my_set2 = {1, 8, 9}
my_set3 = {5, 6, 7}
# sethez hozzáadok
# my_set.add(3)

# # setből törlök
# my_set.pop()
# my_set.remove(4)

temp = my_set.difference(my_set2, my_set3)

print(temp)

temp = my_set.intersection(my_set2)

print(temp)

temp = my_set.issubset(my_set2)

print(temp)

