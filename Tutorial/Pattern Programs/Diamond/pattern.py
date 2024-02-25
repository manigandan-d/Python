#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

n=5

for row in range(1, n*2):
    totColsInRow = n * 2 - row if row > n else row

    noOfSpaces = n - totColsInRow

    for s in range(noOfSpaces):
        print(" ", end="")

    for col in range(totColsInRow):
        print("*", end=" ")
    print()

#         1 
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
#   4 3 2 1 2 3 4
#     3 2 1 2 3
#       2 1 2
#         1
    
n=5

for row in range(1, n*2):
    totColsInRow = n * 2 - row if row > n else row

    noOfSpaces = n - totColsInRow

    for s in range(noOfSpaces):
        print(" ", end=" ")

    for col in range(totColsInRow, 0, -1):
        print(col, end=" ")
    for col in range(2, totColsInRow+1):
        print(col, end=" ")
    print()
