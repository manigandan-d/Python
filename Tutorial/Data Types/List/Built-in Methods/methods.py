data = [5, 10, 15, 20, 25, 30]

print("append -> " + str(data))

data.insert(2, 12)
print("insert -> " + str(data))

data.extend([35, 40, 45])
print("extend -> " + str(data))

dupData = data.copy()
print("copy -> " + str(dupData))

data.remove(45)
print("remove -> " + str(data))

data.pop(2)
data.pop()
print("pop -> " + str(data))

# data.clear()
print("clear -> " + str(data))

print("index -> " + str(data.index(15)))

print("count -> " + str(data.count(5)))

data.sort()
print("sort -> " + str(data))

data.reverse()
print("reverse -> " + str(data))
