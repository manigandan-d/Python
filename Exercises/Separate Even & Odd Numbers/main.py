data = list(range(30))

print(f"Original data: {data}")

eveData = []
oddData = []

for i in data:
    if i % 2 == 0:
        eveData.append(i)
        
    else:
        oddData.append(i)
        
print(f"Even data: {eveData}")
print(f"Odd data: {oddData}")
