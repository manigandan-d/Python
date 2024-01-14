"""
It opens the file in append/write mode if it exists or creates the new file if doesn't exist 
File pointer points to the end of the file 
"""

fobj = open("test.txt", "a")

print(fobj.tell())
fobj.write(" bye")
print(fobj.tell())

fobj.close()

