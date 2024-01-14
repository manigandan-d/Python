def decor(fun):

    def inner(a, b):
        if a < b:
            a, b, = b, a

        return fun(a, b)

    return inner


@decor
def div(a, b):
    print(a / b)


# div = decor(div)
div(2, 5)
