"""
fobj = open("test.txt") - default mode: r
It opens the file in read mode if it exists or raises FileNotFoundError if doesn't exist 
File pointer points to the beginning of the file 
"""

fobj = open("test.txt", "r")

print(fobj.read())

fobj.close()

