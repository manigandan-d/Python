squares = [x**2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(1, 7) if x%2 == 0]
print(evens)

result = [x if x%2 == 0 else -x for x in range(5)]
print(result)
