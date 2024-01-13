# Nested if with list comprehension

data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
res = [i for i in data if i % 5 == 0 if i % 2 == 0]
print(res)
