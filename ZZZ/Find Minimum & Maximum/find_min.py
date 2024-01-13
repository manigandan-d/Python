def findMin(data):
    minVal = data[0]

    for num in data:
        if num < minVal:
            minVal = num

    return minVal


data = [5, 1, 9, 7, 2, 0, 6, 4, 8, 3]

res = findMin(data)

print(f"Minimum value: {res}")
