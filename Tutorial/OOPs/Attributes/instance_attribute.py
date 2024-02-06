class Employee:
    def getInfo(self, name, id):
        self.empName = name
        self.empId = id
        
    def putInfo(self):
        print(self.empName)
        print(self.empId)

emp1 = Employee()
emp1.getInfo("mani", 101)
emp1.putInfo()

print()

emp2 = Employee()
emp2.getInfo("anbu", 102)
emp2.putInfo()
