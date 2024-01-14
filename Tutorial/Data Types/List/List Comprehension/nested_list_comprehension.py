# matrix

matrix = []

for i in range(3):
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print("Without using List Comprehension : {}".format(matrix))

matrix = [[j for j in range(5)] for i in range(3)]

print("Using List Comprehension : {}".format(matrix))

# matrix transpose

m = 3
n = 3

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]


def transpose(X, Y):
    Y = [[i[j] for i in X] for j in range(n)]

    return Y


def display(X):
    for i in range(m):
        for j in range(n):
            print(X[i][j], end=" ")
        print()


print("Original Matrix")

display(A)

B = [[0 for j in range(n)] for i in range(m)]

B = transpose(A, B)

print("Transposed Matrix")

display(B)
