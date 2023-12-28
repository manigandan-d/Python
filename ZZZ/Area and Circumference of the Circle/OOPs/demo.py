import math

class Circle:
	def __init__(self, r):
		self.r = r
		
	def area(self):
		print(math.pi * self.r * self.r)
	
	def circumference(self):
		print(2 * math.pi * self.r)
	


c1 = Circle(5)

c1.area()
c1.circumference()

