class VSCode:
    def execute():
        print("general")
        print("extensions")
        print("compile")
        print("run")

class PyCharm:
    def execute():
        print("specific")
        print("features")
        print("compile")
        print("run")

class Laptop:
    def __init__(self, ide):
        ide.execute()

c_ide = VSCode()
cpp_ide = VSCode()
python_ide = PyCharm()

lap1 = Laptop(c_ide)