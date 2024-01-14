"""
It opens the file in read & write modes and overwrites the file if it exists or creates the new file if doesn't exist
File pointer points to the beginning of the file 
"""

fobj = open("test.txt", "w+")

print(fobj.tell())
fobj.write("hey md")
print(fobj.tell())
fobj.seek(0)
print(fobj.read())

fobj.close()

