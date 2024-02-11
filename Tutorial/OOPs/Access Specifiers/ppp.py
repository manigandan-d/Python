class Demo:
    def __init__(self):
        self.publicAttr = "public attribute"
        self._protectedAttr = "protected attribute"
        self.__privateAttr = "private attribute"
        
    def publicMeth(self):
        print("public method")
        
    def _protectedMeth(self):
        print("protected method")
        
    def __privateMeth(self):
        print("private method")
        
obj = Demo()

print(obj.publicAttr)
obj.publicMeth()

# not recommended 
print(obj._protectedAttr)
obj._protectedMeth()

# error 
# print(obj.__privateAttr)
# obj.__privateMeth()

print(dir(obj))

# accessing private member using name mangling 
print(obj._Demo__privateAttr)
obj._Demo__privateMeth()
