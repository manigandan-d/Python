data = [2, 4, 6, 8, 10]

# for i in data:
#     print(i)


it = iter(data)

# for i in data:
#     print(it.__next__())

for i in data: 
    print(next(it))