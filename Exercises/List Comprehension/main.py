# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a
# cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the
# sum of i+j+k is not equal to n. Here, 0<=i<=x; 0<=j<=y; 0<=k<=z.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    data = []

    [data.append([i, j, k]) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    res = []

    for i in data:
        if sum(i) != n:
            res.append(i)

        else:
            pass

    print(res)

# sample input 0

# 1
# 1
# 2
# 3

# sample input 1

# 1
# 1
# 1
# 2

# sample input 2

# 2
# 2
# 2
# 2

