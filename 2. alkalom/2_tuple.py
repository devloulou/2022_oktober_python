my_string = ''
my_string2 = ""
my_string3 = str()

# tuple - tápl
my_tuple = ()
my_tuple2 = tuple()

# a tuple megváltoztathatatlan - immutable
# nem lehet hozzáadni elemet
# nem lehet törölni belőle elemet
# nem lehet módosítani elemet

my_tuple = (1, 2, 3, 'Ricsi', 'Karcsi', ('alma', 2))
my_tuple = (1, 2, 3, 'Ricsi', ('alma', 2))

my_tuple2 = my_tuple[1:4]

# print(my_tuple[0])
# print(my_tuple[::2])

print(my_tuple2)