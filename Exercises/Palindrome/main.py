data = input("Enter the data: ")

data = data.replace(" ", "").lower()

start = 0
end = len(data) - 1

flag = True

while start < end: 
	if data[start] != data[end]:
		flag = False
		
	start += 1
	end -= 1
	
if flag:
	print(f"{data} is a palindrome")
	
else:
	print(f"{data} is not a palindrome")
