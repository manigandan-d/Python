class Human:
	def __init__(self, name, age):
		print(f"Name: {name} & Age: {age}")
		
	def sleep(self):
		print("I can sleep")
		
	def eat(self):
		print("I can eat")
		
	def work(self):
		print("I can work")
		

class Male(Human):
	def __init__(self, m_name, m_age, pos):
		super().__init__(m_name, m_age)
		print(f"I'm {pos}")
		
	def work(self):
		super().work()
		print("I can code")
		
		
class Female(Human):
	def __init__(self, f_name, f_age, pos):
		super().__init__(f_name, f_age)
		print(f"I'm {pos}")
	
	def work(self):
		super().work()
		print("I can test")
		
		
m1 = Male("md", 22, "coder")

m1.sleep()
m1.eat()
m1.work()

print(Male.mro())
print(Male.__mro__)

f1 = Female("kd", 24, "tester")

f1.sleep()
f1.eat()
f1.work()

print(Female.mro())
print(Female.__mro__)

