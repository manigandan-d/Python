"""
It opens the file in write mode & overwrites the file if it exists or creates the new file if doesn't exist 
File pointer points to the beginning of the file 
"""

fobj = open("test.txt", "w")

fobj.write("Hey MD")

fobj.close()

