details = {"Name": "Mani", "Age": 22, "Gender": 'M'}

print(details.get("Name"))

print(details.keys())

print(details.values())

print(details.items())

# details["Position"] = "Embedded Engineer"

print(details.copy())

details.pop("Gender")
print(details)

details.popitem()
print(details)

details.clear()
print(details)
