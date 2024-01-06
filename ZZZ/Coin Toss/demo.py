import random

data = ["Head", "Tail"]

totalHead = 0
totalTail = 0


def toss_coin():
    return random.choice(data)


for i in range(10):
    res = toss_coin()

    print(f"Toss_{i + 1}: {res}")

    if res == "Head":
        totalHead += 1

    else:
        totalTail += 1

print(f"Total Heads: {totalHead}")
print(f"Total Tails: {totalTail}")
