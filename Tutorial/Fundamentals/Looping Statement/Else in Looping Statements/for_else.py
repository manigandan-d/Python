data = [1, 3, 5, 7, 9]

# data = [2, 4, 6, 8, 10]

for i in data:
    if i % 2 == 0:
        print(i)
        break

else:
    print("There's no even numbers in the data")
