def add(x: int, y: int):
    return x + y

print(add(1, 2))



def add_all(*args):
    print(args)
    print(type(args))

add_all(1, 2, 3)

# * and ** упаковка и распоковка итерабельных обьектов и словарей