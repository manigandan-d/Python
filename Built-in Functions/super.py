class A:
	def __init__(self): 
		self.a1 = 5
		self.a2 = 10
		
	def display(self):
		print(self.a1, self.a2)
		


class B(A):
	def __init__(self):
		super().__init__()
		self.b1 = 3
		self.b2 = 7
		
	def display(self):
		super().display()
		print(self.b1, self.b2) 
		


b_obj = B()

b_obj.display()

