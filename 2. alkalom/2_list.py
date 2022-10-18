# list - lista
# megváltoztatható - mutable
# lehet hozzáadni adatot
# lehet belőle törölni adatot
# lehet módosítani a meglévő adatot

my_list = [1, 2, 3, 4, 'Ricsi', (), [1]]
my_list2 = list()


# listához hozzáadni 1 elemet: append
my_list = []

my_list.append(2022)
my_list.append(2000)


# egy érték hozzáadása, de megadott helyre: insert
my_list.insert(1, 'Ricsi')
#print(my_list)

# egyszerre több elemet hozzáadni a listához: extend

my_list = []

my_list.extend("Almapaprika")

my_list = []

my_list.extend(("Almapaprika", 'Ricsi', 'Ricsi'))

#print(my_list)

#################################################################

# törlés listából

my_list = [1, 2, 3, 4, 5, 6, 7, 10]

#my_list.clear()

# index mentén való törlés: pop()
my_list.pop()
my_list.pop(3)

# érték mentén való törlés: remove()

my_list = [1, 1, 3, 4, 5, 4, 7, 3]
my_list.remove(4)
# my_list.remove(4) 

# del függvény
del my_list[0]


# print(my_list)

###################################################
# lista elemeinek módosítása

my_list = [1, 2, 3, 4, 5]

# egy elem új értékadása
#my_list[2] = 6

my_list[1:4] = 6, 7, 8

# num1, num2, num3 = 4, 5, 6
# print(num1, num2, num3)
#print(my_list)

# figyelni az alábbira
my_list[1:5] = 6, 7

my_list = [1, 2, 3, 4, 5]

my_val_idx = my_list.index(3)
my_list[my_val_idx] = 6

########################################
# referencia
# num1 = 5
# num2 = 5

num1 = 5
num2 = num1
num3 = num2

#num1 = 10

# print(num2)
# print(num3)
# print(num2)
######################################################

my_list = [1, 2, 3, 4, 5]
my_list2 = my_list

my_list.append(6)
my_list.pop(1)


my_list = [1, 2, [1, 2, ['Ricsi', [1, 2]]]]
print(my_list2)
