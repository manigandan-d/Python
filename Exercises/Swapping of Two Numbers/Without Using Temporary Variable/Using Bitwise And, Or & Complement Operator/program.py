a = 5
b = 10

a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1

print(a)
print(b)
