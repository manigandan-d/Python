# Given the names and grades for each student in a class of  students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.

def countX(data, x):
    count = 0

    for i in data:
        if i == x:
            count += 1

    return count


nameData = []
scoreData = []

for i in range(int(input())):
    name = input()
    score = float(input())

    nameData.append(name)
    scoreData.append(score)

scoreDataSorted = sorted(scoreData)

val = 0

temp = scoreDataSorted[0]

for i in scoreDataSorted:
    if i == temp:
        pass

    else:
        val = i
        break

count = countX(scoreDataSorted, val)

res = []

for ind, ele in enumerate(scoreData):
    if ele == val:
        res.append(nameData[ind])

res.sort()

for i in res:
    print(i)

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
