# next(iter, stopdef)

routine = ["sleep", "eat", "exercise", "work", "repeat"]

# list_iterator object

iterRoutine = iter(routine)

# using next() function to iterate

for i in range(len(routine)):
    print(next(iterRoutine, "end"))

print(next(iterRoutine, "end"))

# using while loop

iterRoutine = iter(routine)

while True:
    item = next(iterRoutine, "end")

    if item == "end":
        break

    print(item)
