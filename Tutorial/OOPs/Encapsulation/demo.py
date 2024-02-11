class Person: 
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        if age > 0:
            self.__age = age
            
        else:
            print("Age must be greater than 0")
            
p1 = Person("mani", 22)

print(p1.getName())
print(p1.getAge())

p1.setName("anbu")
p1.setAge(20)

print(p1.getName())
print(p1.getAge())
