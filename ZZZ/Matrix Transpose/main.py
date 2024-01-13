m = 3
n = 3

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]


def transpose(A, B):
    for i in range(m):
        for j in range(n):
            B[i][j] = A[j][i]


def display(X):
    for i in range(m):
        for j in range(n):
            print(X[i][j], end=" ")
        print()


print("Original Matrix")

display(A)

B = [[0 for j in range(n)] for i in range(m)]

transpose(A, B)

print("Transposed Matrix")

display(B)
