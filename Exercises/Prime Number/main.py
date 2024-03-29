import math

def prime_checker(num):
    if num <= 1:
        print(f"{num} is not a prime number")
        
    else:
        for i in range(2, math.ceil(num/2)+1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        
        else:
            print(f"{num} is a prime number") 


num = int(input("Enter the number: "))

prime_checker(num)   
