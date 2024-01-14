def details(name, *data):
    print(name, end=" ")
    for i in data:
        print(i, end=" ")


details("Mani", 22, 'M')


# without using first parameter


def details(*data):
    for i in data:
        print(i, end=" ")


# details("Mani", 22, 'M')
