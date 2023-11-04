from functools import reduce

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data)

evenData = list(filter(lambda a: a % 2 == 0, data))
print(evenData)

doubleData = list(map(lambda a: a * 2, evenData))
print(doubleData)

sumData = reduce(lambda a, b: a + b, doubleData)
print(sumData)
