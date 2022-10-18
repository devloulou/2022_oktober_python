# életszerű példát:
my_dict2 = {
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}

# dictionary: {} és kulcs - érték párokból állnak
# a setnek is {} a "zárójele"
# a dictionary is mutable adattípus - megváltoztatható
# lehet kulcs - érték párokat hozzáadni
# lehet módosítani
# lehet törölni

# a kulcs minden esetben egyedi - SZINTENKÉNT

my_dict = { "auto": "Ford", 
            "color": "blue",
            }

# lekérni egy adott értéket a dictionaryből

# my_list = [1]

# print(my_list[1])

# print(my_dict['auto'])
# print(my_dict['color'])

# print(my_dict.get('price'))

# törlés dictionary-ból

# my_dict.clear()
#my_dict.pop("auto")
#temp = my_dict.popitem()
# del my_dict['color']

# kulcs - érték hozzáadása dictionary-hez

my_dict = { "auto": "Ford", 
            "color": "blue",
            "brand": {
                "brand": "valami"
            } 
            }

my_dict['price'] = 5400
my_dict['cc2'] = 1200

my_dict.update({'motor_type': "diesel", 'cc2': 2000})


# módosítás ugyan az , mint a hozzáadás


my_dict = { "auto": "Ford", 
            "color": "blue",
            "brand": {
                "brand": {
                            "brand": {
                                    "brand": "GM"
                                    }}
            } 
            }


print(my_dict['brand']['brand']['brand']['brand'])


# elágazások és ciklusok
# comprehension kifejezések