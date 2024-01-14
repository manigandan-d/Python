def getSum(n):
    sum = 0

    while n != 0:
        sum += (n % 10)
        n = (n // 10)

    return sum


num = int(input("Enter the number: "))
print(getSum(num))
