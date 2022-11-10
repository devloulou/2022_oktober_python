"""
1. megnyitod a filet valamilyen műveletre
2. elvégzed a file-on a feladatokat
3. amikor végeztél a műveleteddel, akkor bezárod a file-t
"""

# f = open(file_elérézési_út, "a megnyitás módját", [egyéb opcionális lehetőségek, pl. file kódolása])
# a megnyitáshoz szüksége van a file elérési útjára

file_path = r"C:\WORK\2022_oktober_python\8. alkalom\Dracul.txt"

f = open(file_path, "r", encoding="utf-8")

# data = f.read()
# # print(data[0:100])
# # print(f.tell())
# data_list = data.split('\n')

# print(data_list[:10])

data2 = f.readlines()

# print(data2[0:10])
f.close()


# my_email = "kovacs.richard90@gmail.com"

# print(my_email.split("richard"))


###################################################
# file kiírás: "w" mode
my_list = ['1\n', '2\n', '3\n', '4\n', '5\n', "Ricsi"]
my_list = ["Ricsi", "Peti", " ez egy kicsit hosszabb szöveg "]

f = open('test.txt', 'w', encoding="utf-8")

# f.write("ez egy teszt string\n")
# f.writelines(my_list)

my_string = "\n".join(my_list)

f.write(my_string)
print(my_list)

f.close()