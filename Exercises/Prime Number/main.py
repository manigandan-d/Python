# 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

num = int(input("Enter the number: "))

if num <= 1:
    print(f"{num} is not a prime number")
    
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    
    else:
        print(f"{num} is a prime number")    
        