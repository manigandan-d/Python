a = 10


def demo():
    global a
    a = 5

    print("Inside the Function : " + str(a))


demo()
print("Outside the Function : " + str(a))
