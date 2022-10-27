# minden 2-vel osztható számot töröljünk a listából
my_list = [1, 4, 6, 9, 10, 3, 5, 7, 2]

def delete_from_list():
    my_list2 = []
    for item in my_list:
        if (item%2) != 0:
            my_list2.append(item)

    return my_list2

my_list = delete_from_list()

##############################################################################
# adjuk meg azon értékek indexét, ahol az elem string

my_list = [1, 2, 3, 4, "R", 5, 6, 7, "R", 8, "K"]

def get_index_of_list():
    cnt = 0
    for item in my_list:
        if type(item) == str:
            print(cnt, item)

        cnt += 1

# get_index_of_list()
# packing : *args, **kwargs

# unpacking: kicsomagol

my_list = (1, 2, 3)

# a, b, c = my_list
a, *b = my_list

# print(b)


my_list = [1, 2, 3, 4, "R", 5, 6, 7, "R", 8, "K"]

def get_index_of_list():    
    for idx, item in enumerate(my_list):
        if isinstance(item, str):
            print(idx, item)

# get_index_of_list()

###########################################################################
# referencia a pythonban

a = 10
b = a

a = 11

# print(id(a))
# print(id(b))
# print(b)


################

my_list = [1, 2, 3]
my_list2 = my_list

my_list.append(5)

# print(id(my_list))
# print(id(my_list2))

# print(my_list2)

my_tup = (1, 2)
my_tup2 = my_tup

my_tup = (1, 3)

# print(id(my_tup))
# print(id(my_tup2))

# modulok után visszatéri a referenciához
# nested list

my_list = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]
temp = [*my_list, *my_list2]

# print(temp)


###########################################################################
# állítsuk elő a my_list-ben lévő elemek négyzet értékét
my_list = [1, 2, 3, 4, 5]

def test_func(*m_list):
    temp = []
    for item in m_list:
        temp.append(item**2)

    return temp

my_val = test_func(*my_list)

print(my_val)
print(my_list)
print("##############")

def test_func2(m_list):
    for idx, item in enumerate(m_list):
        m_list[idx] = item ** 2

test_func2(my_list)
print(my_list)


######################################################################