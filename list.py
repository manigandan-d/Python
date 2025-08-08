fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.5, True]
empty_list = []

print(fruits[0])
print(fruits[-1])

for fruit in fruits:
    print(fruit, end=" ")

print()

fruits[1] = "mango"

fruits.append("orange")
fruits.insert(1, "mango")

print("mango" in fruits)
index = fruits.index("mango")
count = fruits.count("mango")

print(index)
print(count)

fruits.remove("apple")
fruits.pop()
fruits.pop(1)
del fruits[0]
fruits.clear()

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
