matrix = []

for i in range(3):
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print("Without using List Comprehension : {}".format(matrix))

matrix = [[j for j in range(5)] for i in range(3)]

print("Using List Comprehension : {}".format(matrix))
