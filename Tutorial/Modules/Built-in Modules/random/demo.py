import random

data = [3, 0, 7, 1, 8, 2, 9, 5, 6, 4]

for i in range(100):
    print(random.randint(1, 5))

for i in range(100):
    print(random.randrange(1, 5))

for i in range(100):
    print(random.random())

for i in range(100):
    print(random.uniform(1, 5))

for i in range(100):
    print(random.choice(data))

random.shuffle(data)
print(data)
