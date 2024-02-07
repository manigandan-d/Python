

from math import pi



# __new__() -> called before __init__()

# class Demo:
#     def __init__(self):
#         print("init method")
        
#     def __new__(self):
#         print("new method")
#         var = object.__new__(self) # explicit call of __init__
#         print(self)
#         print(var)
#         return var
        
# d = Demo()
# print(d)

# destructor 
# class Circle:
#     def __init__(self, r):
#         self.radius = r
        
#     def area(self):
#         res = pi * self.radius * self.radius
#         print(res)
        
#     def __del__(self):
#         print("object is deleted")
    
# c1 = Circle(5)
# c1.area()

# # del c1

# __str__()

# num=100
# print(type(num))

# strNum = str(num)
# print(type(strNum))

# strNum = int.__str__(num)
# print(type(strNum))

# attribute

# class Circle:
#     "this ia an example of doc string "
#     def __init__(self, r):
#         self.radius = r
        
#     def area(self):
#         res = pi * self.radius * self.radius
#         print(res)
    
# c1 = Circle(5)
# c1.area()

# print(c1.__doc__)

# decorators - built in and user defined 

# built in decorators - class, static and property decorators 

# class decorator - @classmethod, explicit call, access , bounded to obj

# class Demo:
#     cnt = 100 # class attribute 
    
#     def get(self): # not-static method 
#         self.var = 350
#         print(self.var)
#         print(Demo.cnt)
    
#     @classmethod
#     def classFun(self, msg): # class decorator 
#         print(Demo.cnt)
#         print(msg)
#         # print(self.var) - can't access instance attribute 
    
# d = Demo()
# d.get()
# d.classFun("md")

# static decorator - @staticmethod - explicit call, access , not bounded to obj

class Demo:
    cnt = 100 # class attribute 
    
    def get(self): # not-static method 
        self.var = 350
        print(self.var)
        print(Demo.cnt)
    
    @staticmethod
    def classFun(msg): # class decorator 
        print(Demo.cnt)
        print(msg)
        # print(self.var) - can't access instance attribute 
    
d = Demo()
d.get()
Demo.classFun("md") # we can use _> d.classFun("md") but it's meaningless 

# property decorator 
# getter 

