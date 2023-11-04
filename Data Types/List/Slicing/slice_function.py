data = [10, 2.5, 'A', "Python"]

print(data[slice(0, 2)])
print(data[slice(0, 5)])

print(data[slice(1, 4)])

print(data[slice(3)])

print(data[slice(0, 4)])  # data[::]

print(data[slice(0, 4, 2)])
print(data[slice(-1, -5, -1)])
