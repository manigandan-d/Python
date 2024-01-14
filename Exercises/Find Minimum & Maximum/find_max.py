def findMax(data):
    maxVal = data[0]

    for num in data:
        if num > maxVal:
            maxVal = num
    return maxVal


data = [5, 1, 9, 7, 2, 0, 6, 4, 8, 3]

res = findMax(data)

print(f"Maximum value: {res}")
