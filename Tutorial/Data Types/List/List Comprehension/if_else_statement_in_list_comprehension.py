data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

modData = [i-1 if i % 2 == 0 else i+1 for i in data]

print(modData)
