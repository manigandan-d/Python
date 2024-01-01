class A:
	def display(self):
		print("Hi from A")
		
		
class B:
	def display(self):
		print("Hi from B")
		

class C:
	def display(self):
		print("Hi from C")
	
	
class D:
	def display(self):
		print("Hi from D")
	

class E:
	def display(self):

		print("Hi from E") 	


class F(A, B, C): 
	def display(self):
		print("Hi from F")
		

class G(D, B, E):
	def display(self):
		print("Hi from G")
		
		
class H(D, A):
	def display(self):
		print("Hi from H")
		

class Z(F, G, H):
	def display(self):
		print("Hi from Z")


z = Z()

z.display()









