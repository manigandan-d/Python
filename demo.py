class Human: # base class - parent class - super class 
	def __init__(self, heart):
		self.num_eyes = 2
		self.num_noes = 1
		self.num_heart = heart
	
	def sleep(self):
		print("I can sleep")
		
	def eat(self):
		print("I can eat")
		
	def work(self):
		print("I can work")
		

class Male(Human): # derived class - child class - sub class 
	def __init__(self, name, heart):
		super().__init__(heart)
		self.name = name
	
	def exercise(self):
		print("I can exercise")
		
	def work(self): # method overriding 
		super().work()
		print("I can code")
		
	def display(self):
		print(f"This is {self.name}")
	
male_1 = Male("mani", 1)

male_1.exercise()
male_1.work()

print(male_1.num_eyes)
print(male_1.num_noes)
print(male_1.num_heart)

male_1.display()
 
