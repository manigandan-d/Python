# iteration with list comprehension

data = [i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

print(data)

# double the data

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubleData = [i * 2 for i in data]

print(doubleData)

# square the data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squareData = [i ** 2 for i in data]

print(squareData)

# nested list comprehension - matrix 

matrix = []

for i in range(3):
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print("Without using List Comprehension : {}".format(matrix))

matrix = [[j for j in range(5)] for i in range(3)]

print("Using List Comprehension : {}".format(matrix))

# matrix transpose 

m = 3
n = 3

A = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
	]
			
def transpose(X, Y):
	Y = [[i[j] for i in X] for j in range(n)]

	return Y

def display(X):
	for i in range(m):
		for j in range(n):
			print(X[i][j], end=" ")
		print()

print("Original Matrix")

display(A)

B = [[0 for j in range(n)] for i in range(m)]

B = transpose(A, B)

print("Transposed Matrix")

display(B)

# if statement in list comprehension

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenData = [i for i in data if i % 2 == 0]

print(evenData)

# even list

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenData = [i for i in data if i%2 == 0]

print(evenData)

# odd list

oddData = [i for i in data if i%2 != 0]

print(oddData)

# extract the name of the specified character in the list

names = ["mani", "anbu", "keerai", "kalai", "durai"]

k_names = list()

res = [name for name in names if "k" in name]

print(res)

# if else statement in list comprehension

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

modData = [i-1 if i % 2 == 0 else i+1 for i in data]

print(modData)

# Nested if with list comprehension

data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

res = [i for i in data if i%5 == 0 if i%2 == 0]

print(res)

# ZZZ - matrix transpose 

m = 3
n = 3

A = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
   ]

def transpose(A, B):
	for i in range(m):
		for j in range(n):
			B[i][j] = A[j][i]

def display(X):
	for i in range(m):
		for j in range(n):
			print(X[i][j], end=" ")
		print()

print("Original Matrix")

display(A)

B = [[0 for j in range(n)] for i in range(m)]

transpose(A, B)

print("Transposed Matrix")

display(B)
