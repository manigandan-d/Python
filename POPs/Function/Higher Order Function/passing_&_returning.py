def greet():
    print("Welcome...")


def mani():
    print("Hello Mani")


def hello(fun):
    fun()
    return greet


fun = hello(mani)
fun()
