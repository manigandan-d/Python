data = [1, 4, 7, 9, 2, 7, 1, 3, 7, 9, 4, 5, 0, 3]

# using membership operator

res = list()

for i in data:
    if i not in res:
        res.append(i)

print(res)

# using list comprehension

res = list()

[res.append(i) for i in data if i not in res]
print(res)

# using set

res = list(set(data))
print(res)


