print("Hello, World!")

prog = "Python"
print("Program:", prog)

name = "Adam"
age = 35 
print(f"My name is {name} and I'm {age} years old.")

print("Hello " + name)

print("Python", "is", "awesome", sep=" - ")

print("Hello", end=" ")
print("World")

with open("output.txt", "w") as f: 
    print("Saving this to a file", file=f)
