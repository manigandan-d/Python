# Enter your code here. Read input from STDIN. Print output to STDOUT

data = list(map(int, input().split()))
polynomial = input()

x = data[0]
k = data[1]

polynomial = polynomial.replace("x", str(x))

res = eval(polynomial)

if res == k:
    print(True)
    
else:
    print(False)

