data = [15, 5, 25, 10, 20]

print(sorted(data))
print(sorted(data, reverse=True))

data = ["dddd", "a", "ccc", "bb"]
print(sorted(data, key=len))


def rem(x):
    return x % 7


data = [11, 7, 3, 9, 15]
print(sorted(data, key=rem))
