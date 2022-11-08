#1. feladat: a megadott dictionary-ben javítsátok a name kulcsot title-re
# a megoldás során törekedjetek arra, hogy függvényeket fejlesszünk

# ismerjük a dictionary szerkezetét

my_dict = {
    "game": {
        "action": [
            {"title": "Call of Duty"},
            {"title": "Battlefield"},
            {"name": "Need for Speed"}
        ],
        "rpg": [
            {"title": "Oblivion"},
            {"title": "Dark Souls"}
        ],
        "arcade": [{"name": "Need for Speed"}]
    }
}


# print(my_dict['game']['action'][2].keys())
# my_dict.values()

# for key, value in my_dict.items():
#     print(value)

def my_func():
    for key, value in my_dict['game'].items():
        for item in value:
            if not item.get('title'):
                item['title'] = item['name']
                item.pop("name")

# my_func()
# print(my_dict)

def my_func():
    for d_item in my_dict['game']:
        for item in my_dict['game'][d_item]:
            if not item.get('title'):
                item['title'] = item['name']
                item.pop("name")




# my_dict['game']['action'][2]["title"] = my_dict['game']['action'][2]["name"]
# my_dict['game']['action'][2].pop("name")

# print(my_dict)

# 2. feladat: Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!

def my_func(a, b, c):
    if a+b==c:
        return True
    elif b+c==a:
        return True
    elif a+c==b:
        return True
    else:
        return False
    return a+b==c or b+c==a or a+c==b

# print(my_func(1,3,3))

# my_val = input("kérlek \nadj meg egy számot\n")

# try:
#     my_val = int(my_val)
# except Exception as e:
#     # itt kezelem szofisztikáltan
#     my_val = -1
# print(type(my_val))
# print(my_val)


# 3. feladat: Írjatok egy olyan függvényt, ami az alább megadott 2 dictionaryből egy harmadikat készít - merge-li őket -

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

def my_func():
    dict1.update(dict2)
    return 
    return dict1 | dict2
    return {**dict1, **dict2}

# print(my_func())
# print(dict1)

# 4. feladat: írjatok egy olyan függvényt, amely az alábbi dictionary-ben,
# az értékek közzül csak azokat hagyja meg,
# amelyek semelyik másik listában nem szerepel

# Példa:
# test_dict = {'ricsi': [1], 'norbi': [1,2,3]}
# my_func(test_dict)
# output: {'ricsi': [], 'norbi': [2,3]}
#

test_dict = {'Jolán' : [1, 4, 5, 6],
            'Ibolya' : [1, 8, 9],
            'Jácint': [10, 22, 4],
            'Karcsi': [5, 11, 22],
            # 'Pista': [8, 1, 4, 40]
            }

#{'Jolán': [6], 'Ibolya': [8, 9], 'Jácint': [10], 'Karcsi': [11]}

# 1. lépés: minden listán végigiterálok és a benne lévő értékeket a többi listához megnézem



print(len(test_dict))
def my_func():
    cnt = -1
    solution = {}
    for key, value in test_dict.items():        
        cnt += 1
        temp = []
        for idx, item in enumerate(list(test_dict.values())):
            if cnt == idx:
                continue
            for v_item in value:
                if v_item in item:
                    continue
                temp.append(v_item)   
        temp2 = []
        for j in set(temp):
            if temp.count(j) == len(test_dict) - 1:
                temp2.append(j) 
        solution[key] = temp2

    return solution


# print(my_func())
test_dict = {'Jolán' : [1, 4, 5, 6],
            'Ibolya' : [1, 8, 9],
            'Jácint': [10, 22, 4],
            'Karcsi': [5, 11, 22],
            # 'Pista': [8, 1, 4, 40]
            }


def my_func():
    cnt = -1
    solution = {}
    for key, value in test_dict.items():        
        cnt += 1
        temp = []
        for idx, item in enumerate(list(test_dict.values())):
            if cnt == idx:
                continue      
                  
            set_value = set(value)
            set_item = set(item)
            nums = set_value.intersection(set_item)
            
            if len(nums) > 0:
                temp.append(list(nums)[0])
        solution[key] = [item for item in value if item not in temp]

    return solution

print(my_func())