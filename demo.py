import re

pwd = input("Enter the password: ")

pwdLen = len(pwd)

isValid = False

while True:
	if pwdLen < 7 or pwdLen > 20:
		break
		
	elif not re.search("[A-Z]", pwd):
		break
		
	elif not re.search("[a-z]", pwd):
		break
		
	elif not re.search("[0-9]", pwd):
		break
		
	elif not re.search("[$#@!]", pwd):
		break
		
	elif re.search("\s", pwd):
		break
		
	else:
		isValid = True
		break

if isValid == True:
	print("Password is valid")
	
else:
	print("Password is invalid")

