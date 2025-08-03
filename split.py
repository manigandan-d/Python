text = "Python is easy"
words = text.split()
print(words)
print(type(words))

data = "apple, banana, mango"
fruits = data.split(", ")
print(fruits)

text = "one two three four five"
parts = text.split(" ", 3)
print(parts)

user_input = input("Enter values separated by comma: ")
values = user_input.split(",")
print(values)
