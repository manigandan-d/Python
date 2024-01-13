n = int(input())

arr = list(map(int, input().split()))

res = list(set(sorted(arr, reverse=True)))

print(res[1])

# 5
# 2 3 6 6 5
