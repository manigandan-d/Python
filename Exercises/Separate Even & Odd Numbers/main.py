data = list(range(30))

print(data)

eveData = []
oddData = []

for i in data:
    if i % 2 == 0:
        eveData.append(i)
        
    else:
        oddData.append(i)
        
print(eveData)
print(oddData)
