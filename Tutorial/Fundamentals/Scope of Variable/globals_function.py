a = 10


def demo():
    a = 5
    print("Inside the Function -> Local Variable : " + str(a))

    globals()["a"] = 5
    print("Inside the Function -> Global Variable : " + str(globals()["a"]))


demo()
print("Outside the Function : " + str(a))
