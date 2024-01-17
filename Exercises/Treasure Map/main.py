line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]

trMap = [line1, line2, line3]

print(f"{line1}\n{line2}\n{line3}")

pos = input("Enter the position where you want to hide your treasure: ")

p1 = int(pos[0]) - 1
p2 = int(pos[1]) - 1

trMap[p1][p2] = "❌"

print(f"{line1}\n{line2}\n{line3}")
