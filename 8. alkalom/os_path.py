import os

print(__file__)

# "c:\WORK\2022_oktober_python\8. alkalom\Dracula.txt"
# "c:\WORK\2022_oktober_python\8. alkalom\os_path.py"

my_path = __file__.split('\\')
my_path[-1] = "Dracula.txt"
my_path = "\\".join(my_path)

with open(my_path, "r", encoding="utf-8") as f:
    data = f.read()

# print(data[0:100])


###################################################################################
print("-----------------------")
import os

# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))

my_string = r"ricsi\karcsi\joci\valami.csv"

# print(os.path.exists(__file__))
# print(os.path.exists(my_string))
# print(os.path.basename(my_string))
# print(os.path.dirname(my_string))

# print(my_string.split('\\')[-1])
# print("\\".join(my_string.split('\\')[:-1]))


my_path = os.path.dirname(__file__) + "\Dracula.txt"
my_path = f"{os.path.dirname(__file__)}\Dracula.txt"
my_path = os.path.join(os.path.dirname(__file__), "Dracula.txt")

# print(my_path)

##########################################################

my_files = [os.path.join(os.path.dirname(__file__), item) for item in os.listdir(os.path.dirname(__file__))]

print(my_files)
for item in my_files:
    print(os.path.exists(item))


