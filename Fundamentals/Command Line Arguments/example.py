import sys

argc = len(sys.argv)

print("Number of Command Line Arguments : " + str(argc))

print("File Name : " + sys.argv[0])

print("Command Line Arguments : ", end="")

for i in range(1, argc):
    print(sys.argv[i], end=" ")
