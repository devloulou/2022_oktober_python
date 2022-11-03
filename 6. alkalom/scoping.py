#scoping - láthatóság

# built-in szint: ő legnagyobb, őt mindenki láthatja, bárhol bármikor
# pl. print függvény, enumerate, stb..


# global szint:

my_list = []

num = 10

def my_func():
    my_list.append("Ricsi")


def my_func():
    b = 10
    def my_sub_func(): #enclosing scope - szint
        a = 5          # local scope - local szint
        print(a*b)
                    
    my_sub_func()
    print(b)

my_func()
