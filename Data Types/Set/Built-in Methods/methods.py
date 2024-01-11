data = {10, 2.5, 'A', "Python"}
proLang = {"C", "C++", "Java"}

data.add(True)
print(data)

dupData = data.copy()
print(dupData)

data.update(proLang)
print(data)

data.remove(True)
print(data)

data.discard('A')
print(data)

data.pop()
print(data)

data.clear()
print(data)

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {2, 4, 6, 8, 10}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.issuperset(B))
print(B.issubset(A))
print(A.isdisjoint(B))
