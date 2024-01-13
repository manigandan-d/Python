routine = ["sleep", "eat", "exercise", "work", "repeat"]

# enumerate object

print(type(enumerate(routine)))

# converting enumerate object into list

print(list(enumerate(routine)))

# enumerate(iterable, start=0)

for count, ele in enumerate(routine):
    print(count, ele)

# setting the start value as 100

for count, ele in enumerate(routine, 100):
    print(count, ele)

# enumerate() with next()

enumRoutine = enumerate(routine)

for i in range(len(routine)):
    print(next(enumRoutine))
