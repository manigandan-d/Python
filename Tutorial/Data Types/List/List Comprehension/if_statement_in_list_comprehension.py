# even list

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenData = [i for i in data if i % 2 == 0]
print(evenData)

# odd list

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddData = [i for i in data if i % 2 != 0]
print(oddData)

# extract the name of the specified character in the list

names = ["mani", "anbu", "keerai", "kalai", "durai"]

k_names = list()

res = [name for name in names if "k" in name]

print(res)
