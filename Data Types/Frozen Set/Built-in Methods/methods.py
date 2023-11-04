data = {10, 2.5, 'A', "Python", 2.5, 10}

frozenData = frozenset(data)
print(frozenData)

dupData = frozenData.copy()
print(dupData)

A = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
B = frozenset({2, 4, 6, 8, 10})

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.issuperset(B))
print(B.issubset(A))

del data
del frozenData
