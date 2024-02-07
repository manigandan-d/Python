# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474

num = int(input("Enter the number: "))

temp = num

cnt = 0
sum = 0

while temp != 0:
    cnt += 1
    temp //= 10

temp = num

for i in range(cnt):
    digit = temp % 10
    sum += (digit ** cnt)
    temp //= 10
    
if sum == num:
    print(f"{num} is an Armstrong number")
    
else: 
    print(f"{num} is not an Armstrong number")