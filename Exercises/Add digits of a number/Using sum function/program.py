def getSum(num):
    listOfNum = list(map(int, num))

    return sum(listOfNum)


num = input("Enter the number: ")
print(getSum(num))
