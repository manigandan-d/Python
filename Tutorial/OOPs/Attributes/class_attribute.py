class Employee:
    empId = 100
    
    def genEmpId(self):
        Employee.empId += 1
        
    def putEmpId(self):
        print(Employee.empId)
        

emp1 = Employee()
emp1.genEmpId()
emp1.putEmpId()

emp2 = Employee()
emp2.genEmpId()
emp2.putEmpId()

print(Employee.empId)
