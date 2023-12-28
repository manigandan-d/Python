import math

class Circle:
	pi = math.pi
	
	def __init__(self, r=5):
		self.r = r
		
	def area(self):
		print(Circle.pi * self.r * self.r)
	
	def circumference(self):
		print(2 * Circle.pi * self.r)
	


c1 = Circle(5)

c1.area()
c1.circumference()

c2 = Circle(10)

c2.area()
c2.circumference()

