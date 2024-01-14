name1 = input("Enter your name: ").lower()
name2 = input("Enter your partner name: ").lower()

name = name1 + name2

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

true = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

love = l + o + v + e

lovePct = str(true) + str(love)

print(f"Your love score: {lovePct}%")
