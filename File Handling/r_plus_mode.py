"""
It opens the file in read & write modes if it exists or raises FileNotFoundError if doesn't exist 
File pointer points to the beginning of the file 
"""

fobj = open("test.txt", "r+")

print(fobj.tell())
print(fobj.read())
fobj.seek(0)
fobj.write("Hey MD")
print(fobj.tell())
print(fobj.read())
print(fobj.tell())

fobj.close()

