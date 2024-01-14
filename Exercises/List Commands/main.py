if __name__ == '__main__':
    N = int(input())

    res = []
    data = []

    commands = ["insert", "append", "remove", "pop", "sort", "reverse", "print"]

    for i in range(N):
        n = input().split()

        for i in n:
            data.append(i)

        if data[0] == "insert":
            res.insert(int(data[1]), int(data[2]))

        elif data[0] == "append":
            res.append(int(data[1]))

        elif data[0] == "remove":
            res.remove(int(data[1]))

        elif data[0] == "pop":
            res.pop()

        elif data[0] == "sort":
            res.sort()

        elif data[0] == "reverse":
            res.reverse()

        elif data[0] == "print":
            print(res)

        data.clear()

# finding the percentage

if __name__ == '__main__':
    n = int(input())

    student_marks = {}
    data = []

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))

        student_marks[name] = scores

    query_name = input()

    for i in student_marks:
        if i == query_name:
            data = student_marks[i]

    tot = sum(data)
    n = len(data)

    avg = tot / n

    print(format(avg, ".2f"))


# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
#
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
