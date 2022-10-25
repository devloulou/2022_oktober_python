# generator objektum - generator expression
# generator expression - lazy evalutaion - laza kiértékelést: nem értékeli ki futási időben a megadott
# kifejezést
# list comprehension pedig teljesen kiértékeli futási időben a megadott kifejezést

# memória hatékony ellenben lassú -> nagy adatfeldolgozás, nagy file-ok kezelése
# nagy számokkal való munkavégzés


from sys import getsizeof


my_gen = (item for item in range(100))
my_list = [item for item in range(100)] # list comprehension

# print(my_gen)
# print(my_list)

# print(getsizeof(my_gen))
print(getsizeof(my_list))


# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# # print(next(my_gen))
# print(next(my_gen))

print("############################")
for item in my_gen:
    print(item)
    print(getsizeof(my_gen))
