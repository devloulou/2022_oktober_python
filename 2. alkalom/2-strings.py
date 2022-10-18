# stringek

# minden olyan adat, amely vagy ' vagy " aposztróf között található, megfel
# "szöveg" kifejezésnek: betük, számok, írásjelek, speciális karakterek
# stringeknek nevezzük

# string az karakterekből áll
# a string megváltoztathatatlan addattípus

## a string iterálható "objektum" -> string iterable object
## string formázással - string formatting

my_string = 'Indul a görög aludni'
my_string2 = "Magyarország előre megy, nem hátra"

# slicing - "szeletelést"

# slicing egy olyan művelet, ahol egy stringből egy megadott művelettel rész
# stringet / karaktereket / karaktert tudok extraktálni -> kiszedni
# slicing: string_neve[tól:ig:lépték_mértéke]

# egy adott index mentén lekérek egy karaktert

# print(my_string[0])

# görög
#print(my_string[8:13])

my_string = 'Indul a görög aludni'
# minden második karaktert
#print(my_string[::2])

#print(my_string[::3])

# irassuk ki az utolsó elemet
# print(my_string[-1])
# print(my_string[-4])

# print(my_string[5:-4])
my_string = 'Indul a görög aludni'
print(my_string[::-1])

my_string2 = "Magyarország előre megy, nem hátra"

print(my_string2[13::2])


