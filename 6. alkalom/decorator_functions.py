# decorator: olyan függvények, amelyek plusz tulajdonságot adnak hozzá 
# meglévő függényekhez, anélkül, hogy változtatnának az eredeti függvényen

# mire jó a decorator, mikor illetve milyen célre célszerű használni:

# logolás
# futási idő mérés
# debugolás
# register
# lassítani a futáson
# caching mechanizmus


printer = print

# printer("Ricsi")

def my_func(func, name):
    
    func(f"{name}")

# my_func(print, "Ricsi")
###################################################

def my_func():
    print("sziasztok")


def start_end_decor(func):
    def wrapper():
        print("Start")
        func()
        print("finish")
    wrapper()

# test = start_end_decor(my_func)


def start_end_decor(func):
    def wrapper():
        print("Start")
        func()
        print("finish")
    return wrapper


def time_it(func):
    from time import time, sleep
    def wrapper(*args, **kwargs):
        start_time = time()
        retval = func(*args, **kwargs)
        sleep(1)
        print(time()-start_time)
        return retval
    return wrapper

@time_it
def add_numbers(num1, num2):
    return num1 + num2

# solution = add_numbers(num1=2, num2=3)
# print(solution)



# decorator függvény: @
@time_it
@start_end_decor
def countdown():
    num = 10
    while num > 0:
        print(num)
        num -= 1

# countdown()

def repeat(cnt_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            retval = 0
            for _ in range(cnt_times):
                retval = func(*args, **kwargs)
            return retval
        return wrapper
    return decorator_repeat


@repeat(4)
def my_func(name):
    print(f"hello {name}")

my_func("Amanda")

# @repeat(5)
# def my_func(num1, num2):
#     return num1 + num2


# print(my_func(2, 3))