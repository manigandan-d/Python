def getSum(num):
    sum = 0

    for i in num:
        sum += int(i)

    return sum


num = input("Enter the number: ")

print(getSum(num))
