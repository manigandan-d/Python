"""
Exclusive Creation Mode 'x'
It creates a new file if doesn't exist or raises a FileExistsError if the file already exists
"""

fobj = open("test.txt", "x")

