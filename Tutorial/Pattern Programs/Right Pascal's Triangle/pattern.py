# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n=5

for row in range(1, n*2):
    totColsInRow = n * 2 - row if row > n else row

    for col in range(totColsInRow): 
        print("*", end=" ")
    print()
