# string formázás

# 4 módszert

# általános módszer:
# 


my_string = "Nevem Ricsi"
my_age = 32

# concatenation - konkatenáció - összefüzés
answer = my_string + " és " + str(my_age) + " éves vagyok"

my_list = ["Ricsi", "Karcsi"]

my_string = ", ".join(my_list)

# A két emberem: Ricsim, Karcsi
answer = "A két emberem: " + my_string

# print(answer)
# nevem Ricsi és 32 éves vagyok


# 1. módszer: "régi módszer" %

my_num = 5043636346346

my_hex_val = "my_num hex value: %x" % my_num

# print(my_hex_val)


my_string = "Nevem Ricsi"
my_age = "%x" % 32


answer = "%s és %s éves vagyok" % (my_string, my_age)

answer = "%(my_string)s és %(my_age)i éves vagyok" % {'my_age': my_age, 'my_string': my_string}

################################################################

# 2. "New Style" string formatting: str.format()

my_string = "Nevem Ricsi"
my_age = 32

answer = "{stringecske} és {age} éves vagyok".format(stringecske=my_string, age=my_age)

print((answer))

##########################################################
# 3. string interpoláció - f-string: f'  vagy f"

my_string = "Nevem Ricsi"
my_age = 32

answer = f"{my_string} és {my_age} éves vagyok"

print(answer)


answer = "{stringecske} és {age} éves vagyok"

print(answer.format(stringecske="RICSI vagyok", age=32))

# template használat

from string import Template

my_template = Template('$name vagyok és $age éves')

print(my_template.substitute(name="Ricsi", age=32))

###############################################################################################