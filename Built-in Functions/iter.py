# iter(object, sentinel)

routine = ["sleep", "eat", "exercise", "work", "repeat"]

# list_iterator object

iterRoutine = iter(routine)
print(type(iterRoutine))

# using __next__() method to iterate

for i in range(len(routine)):
    print(iterRoutine.__next__())

iterRoutine = iter(routine)

# using next() function to iterate

for i in range(len(routine)):
    print(next(iterRoutine))
