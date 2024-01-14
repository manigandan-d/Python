stmt = "This is MANIGANDAN D"

print("upper -> " + stmt.upper())
print("isupper -> " + str(stmt.isupper()))

print("lower -> " + stmt.lower())
print("islower -> " + str(stmt.islower()))

print("title -> " + stmt.title())
print("istitle -> " + str(stmt.istitle()))

print("capitalize -> " + stmt.capitalize())

print("swapcase -> " + stmt.swapcase())

print("find -> " + str(stmt.find("i")))
print("rfind -> " + str(stmt.rfind("i")))

print("count -> " + str(stmt.count("i")))

print("strip -> " + stmt.strip())
print("lstrip -> " + stmt.lstrip())
print("rstrip -> " + stmt.rstrip())

print("removeprefix -> " + stmt.removeprefix("This"))
print("removesuffix -> " + stmt.removesuffix("GANDAN D"))

print("replace -> " + stmt.replace(" ", ""))

print("split -> " + str(stmt.split()))
print("rsplit -> " + str(stmt.rsplit()))

print("join -> ", "-".join(stmt))

print("isdecimal -> " + str(stmt.isdecimal()))
print("isdigit -> " + str(stmt.isdigit()))
print("isnumeric -> " + str(stmt.isnumeric()))

print("isalpha -> " + str(stmt.isalpha()))
print("isalnum -> " + str(stmt.isalnum()))

print("startswith -> " + str(stmt.startswith('T')))
print("endswith -> " + str(stmt.endswith('D')))

print("center -> " + stmt.center(50, "*"))
print("ljust -> " + stmt.ljust(50, "*"))
print("rjust -> " + stmt.rjust(50, "*"))
