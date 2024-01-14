def fun(n):
    if n == 0:
        return

    else:
        print(n, end=" ")

    return fun(n - 1)


n = 5
fun(n)
