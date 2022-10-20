# for loop - for ciklust - elöltesztelős ciklus
"""
my_list = [1, 2]
for (int i; i >= my_list.lenght(); i++) {
    System.Out.Prinln(i);
};

"""


"""
for ciklusváltozó in iterálható_object:
    csinálom a dolgokat
    csinálom a vizsgálatokat
    stb.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for item in my_list:
#     if item%2==0:
#         print(item)


# hogyan lehet vezérelni a ciklusokat
# ki tudunk lépni belőle manuálisan
# rá tudjuk venni, hogy a következő ciklusra ugorjon


my_list = [4, 3, 6, 5, 3, 2, 7, 10]

# break megállítja és kilépteti a ciklust a futásából
for item in my_list:
    #print(item)
    break

print()
for item in my_list:
    if item == 5:
        continue
    #print(item)


for item in my_list:
    if item%2 == 0:
        pass
        #print(item)
    else:
        pass

for item in my_list:
    pass

####################################################################################

my_list = []
for item in range(0, 100, 10):
    my_list.append(item)
    

#comprehension műveletek
# list comprehension, generator comprehension, dictionary comprehension
my_list = []
my_list = [item for item in range(0, 100, 10)]

gen_comp = (item for item in range(0, 100, 10))

dict_comp = {str(item)+"key": item for item in range(0, 100, 10)}

print(gen_comp)

# generator object
# set
# mik azok a függvények
# lists, dictionary, for ciklus




