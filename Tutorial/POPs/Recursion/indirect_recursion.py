n = 1


def odd():
    global n
    if n <= 10:
        print(n + 1, end=" ")
        n += 1
        even()


def even():
    global n
    if n <= 10:
        print(n - 1, end=" ")
        n += 1
        odd()


odd()
