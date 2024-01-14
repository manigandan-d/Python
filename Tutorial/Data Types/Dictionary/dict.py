details = {"Name": "Mani", "Age": 22, "Gender": 'M'}

print(details)
print()

for i in details:
    print(i)

print()

for key in details.keys():
    print(key)

print()

for value in details.values():
    print(value)

print()

for key, value in details.items():
    print(key, end=":")
    print(value)

del details
