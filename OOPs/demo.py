# class name should be in PascalCase

class Demo:
	z = 122 # class attribute 
	
	def __init__(self, a, ch): 
		self.a = a
		self.ch = ch
		# self.z = 122
	

d1 = Demo(5, 'A')

print(d1.a, d1.ch, d1.z)

d2 = Demo(10, 'B')

print(d2.a, d2.ch, d2.z)

