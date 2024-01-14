class Human:
	def __init__(self, a):
		self.hvar = a
	
	def sleep(self):
		print("I can sleep")
		
	def eat(self):
		print("I can eat")
		
	def work(self):
		print("I can work")

		
class Male:
	def __init__(self, b):
		self.mvar = b
	
	def exercise(self):
		print("I can exercise")
		
	def work(self):
		print("I can code")
		

class Boy(Human, Male):
	def __init__(self, a, b, c):
		super().__init__(a)
		Male.__init__(self, b)
		self.bvar = c
	
	def work(self):
		# super().work()
		# Male.work(self)
		print("I can test")
	
	
b1 = Boy(5, 10, 15)

b1.sleep() # Boy.sleep(b1)
b1.exercise()
b1.work()

# Human.work(b1)
# Male.work(b1)

# Method Resolution Order 

# print(Boy.mro())
# print(Boy.__mro__)

print(b1.hvar)
print(b1.mvar)
print(b1.bvar)

