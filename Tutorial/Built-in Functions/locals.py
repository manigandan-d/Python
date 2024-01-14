a = 10


def demo():
    b = 5
    c = 2
    d = 1

    print(locals())  # locals() in Local Scope

    locals()["b"] = 15  # Unlike globals(), locals() can not modify the data of the local symbol table

    print(locals())


demo()

print(globals())

print(locals())  # locals() in Global Scope acts as globals()
