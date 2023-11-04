from math import pi

# String Formatting

name = "Mani"
proLang1 = "C"
proLang2 = "C++"
proLang3 = "Python"
proLang4 = "Java"

print("{} knows {}, {}, {} & {}".format(name, proLang1, proLang2, proLang3, proLang4))
print("{0} knows {3}, {1}, {4} & {2}".format(name, proLang1, proLang2, proLang3, proLang4))
print("{n} knows {p1}, {p2}, {p3} & {p4}".format(n=name, p1=proLang1, p2=proLang2, p3=proLang3, p4=proLang4))

# Padding

print("***{}***".format(name))
print("***{:10}***".format(name))
print("***{:^10}***".format(name))
print("***{:<10}***".format(name))
print("***{:>10}***".format(name))

# Set Precision

print(pi)
print("{:.2f}".format(pi))
