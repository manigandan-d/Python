# 0 1 1 2 3 5 8 13 21 ...

n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")

elif n == 1:
    print(a)
    
else:
    print(a)
    print(b)
    
    for i in range(2, n):
        c = a + b
        a, b = b, c
        
        print(c)
