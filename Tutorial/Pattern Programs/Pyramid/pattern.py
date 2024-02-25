#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

n=5

for row in range(1, n+1):
    noOfSpaces = n - row

    for s in range(noOfSpaces):
        print(" ", end=" ")

    for col in range(row, 0, -1):
        print(col, end=" ")
    for col in range(2, row+1):
        print(col, end=" ")
    print()
