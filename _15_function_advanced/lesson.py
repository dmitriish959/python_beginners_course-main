def add(x: int, y: int):
    return x + y

print(add(1, 2))



def add_all(*args):
    print(args)
    print(type(args))

add_all(1, 2, 3)

# * and ** упаковка и распоковка итерабельных обьектов и словарей


def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))


introduce(name="John", age=30, city="New York")


# Запихиваем словарь в функцию introduce
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

introduce(**person)


# функция которая принимает все варианты аргументов

def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs )
    print(x, y)
    print(args)
    print(value)
    print(kwargs)

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}


func_with_all_arguments(1, 2, 3, 4, 5, **person)

# Функция умее возвращать сразу несколько значений
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items()
        if old_dict.get(key) != value:
            old.dict(key) = value
            is_modified = True

    return old_dict, is_modified

produc = {'id': 1, 'name': 'Laptop', 'price': 999.99}

structure = modify_dict(old.dict=product, in_stoks=True)

print(structure)
print(type(structure))






