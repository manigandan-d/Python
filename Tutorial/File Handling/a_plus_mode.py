"""
It opens the file in append/write & read modes if it exists or creates the new file if doesn't exist 
File pointer points to the end of the file 
"""

fobj = open("test.txt", "a+")

print(fobj.tell())
fobj.seek(0)
print(fobj.read())
fobj.write(" bye")
print(fobj.tell())
fobj.seek(0)
print(fobj.read())

fobj.close()

