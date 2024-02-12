data = list(map(int, input().strip()))

x = data[0]
k = data[1]

res = x ** 3 + x ** 2 + x + 1

if res == k:
    print(True)
    
else:
    print(False)