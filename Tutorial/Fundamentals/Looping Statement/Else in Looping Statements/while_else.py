data = [1, 3, 5, 7, 9]

# data = [2, 4, 6, 8, 10]

i = 0
n = len(data)

while i < n:
    if data[i] % 2 == 0:
        print(i)
        break

    i += 1

else:
    print("There's no even numbers in the data")
