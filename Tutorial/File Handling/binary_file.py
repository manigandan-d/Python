fobj1 = open("boards.jpg", "rb")
fobj2 = open("boards_clone.jpg", "wb")

for i in fobj1:
	fobj2.write(i)
	
fobj1.close()
fobj2.close()

