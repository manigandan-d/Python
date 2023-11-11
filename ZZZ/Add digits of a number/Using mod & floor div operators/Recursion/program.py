def getSum(n):
    return 0 if n == 0 else (n % 10) + getSum(n // 10)


num = int(input("Enter the number: "))
print(getSum(num))
