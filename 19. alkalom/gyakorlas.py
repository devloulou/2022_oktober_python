# 1. feladat:

my_list = [1, 2, 3, 4, 5, 6]
my_list2 = [2, 3, 4, 7]

solution = []

# scope
def merge_list():    
    for item in my_list2:
        if item not in my_list:
            solution.append(item)

    solution.extend(my_list)

    return solution

# merge_list()

# print(solution)

def merge_list():
    return list(set([*my_list, *my_list2]))

# print(merge_list())

############################################################################
#########
# 2. feladat:

my_dict = {
    "data": [
        {
            "brand": "BMW",
            "color": "red",
            "price": 100_000_000
        }
    ]
}

my_list = [('Trabant', 'blue', 10_000), ('Opel', 'black', 1_000_000)]



def upload_dict():
    for item in my_list:
        my_dict['data'].append({
            "brand": item[0],
            'color': item[1],
            "price": item[2]

        })

upload_dict()


# print(my_dict)

my_list = ('Trabant', 'blue', 10_000)

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

########################################################################

# 3. feladat:


