def outer():
    a = 10

    def inner():
        a = 5

    inner()
    print(a)


print("Value of a without using nonlocal keyword : ", end="")
outer()


def outer():
    a = 10

    def inner():
        nonlocal a
        a = 5

    inner()
    print(a)


print("Value of a using nonlocal keyword : ", end="")
outer()
