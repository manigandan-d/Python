# * 
# * *
# * * *
# * * * *
# * * * * *

n=5

for row in range(n):
    for col in range(row+1):
        print("*", end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

n=5

for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()