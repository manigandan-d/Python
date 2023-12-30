class Human:
	def __init__(self, a):
		self.hvar = a
	
	def sleep(self):
		print("I can sleep")
		
	def eat(self):
		print("I can eat")
			
	def work(self):
		print("I can work")
		
		
class Male(Human):
	def __init__(self, b):
		self.mvar = b
	
	def work(self):
		print("I can code")
	
	def exercise(self):
		print("I can exercise")
		
		
class Boy(Male):
	def __init__(self, a, b, c):
		Human.__init__(self, a)
		super().__init__(b)
		self.bvar = c
	
	def work(self):
		Human.work(self)
		super().work()
		print("I can test")
		
	def investment(self):
		print("I can invest")
		
		
b1 = Boy(5, 10, 15)

b1.sleep()
b1.exercise()
b1.investment()

b1.work()

print(b1.hvar)
print(b1.mvar)
print(b1.bvar)

print(Boy.mro())
print(Boy.__mro__)

