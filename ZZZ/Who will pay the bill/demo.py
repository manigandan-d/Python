import random

data = input("Enter everybody's name: ")

dataSplit = data.split()

res = random.choice(dataSplit)

print(f"{res} will pay the bill")
