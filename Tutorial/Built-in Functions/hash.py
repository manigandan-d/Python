# hash(obj) -> obj should be immutable

intData = 10
print(hash(intData))

floatData = 5.2
print(hash(floatData))

strData = "python"
print(hash(strData))

# listData = [1, 2, 3, 4, 5]
# print(hash(listData))

tupleData = (1, 2, 3, 4, 5)
print(hash(tupleData))

# dictData = {1: "abc", 2: "xyz"}
# print(hash(dictData))

# setData = {1, 2, 3}
# print(hash(setData))
