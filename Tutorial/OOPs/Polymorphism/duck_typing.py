# duck test -> if it looks like a duck, swims like a duck and quacks like a duck then it probablu is a duck

class VSCode:
    def execute(self):
        print("general")
        print("extensions")
        print("compile")
        print("run")

class PyCharm:
    def execute(self):
        print("specific")
        print("features")
        print("compile")
        print("run")

class Laptop:
    def code(self, ide):
        ide.execute()

cpp_ide = VSCode()
python_ide = PyCharm()

lap1 = Laptop()
# lap1.code(cpp_ide)
lap1.code(python_ide)
