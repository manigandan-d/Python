data = input("Enter the heights: ")

dataList = data.split()

# dataListInt = list()

n = len(dataList)

for i in range(n):
    dataList[i] = int(dataList[i])

total = sum(dataList)

res = round(total / n)

print(f"Average of heights: {res}")
