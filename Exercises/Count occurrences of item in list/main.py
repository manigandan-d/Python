def countX(lst, x):
    cnt = 0

    for i in lst:
        if i == x:
            cnt += 1

    return cnt


data = [1, 9, 2, 0, 3, 6, 4, 9, 2, 0, 4, 7, 5, 8, 3, 7, 1, 8, 3, 9, 1, 8, 2, 7]

# using count method

count = data.count(1)
print(count)

# using user defined function

count = countX(data, 1)
print(count)

# using list comprehension

temp = [i for i in data if i == 1]
print(len(temp))

# using dictionary comprehension

temp = {i: data.count(i) for i in data}
print(temp.get(1))
