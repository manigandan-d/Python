class A:
	def display(self):
		print("Hi from A")
		
		
class B(A):
	def display(self):
		super().display()
		print("Hi from B")
		

class C(B):
	def display(self):
		super().display()
		# A.display(self)
		print("Hi from C")
	
	
class D:
	def display(self):
		print("Hi from D")
	

class E(A, D):
	def display(self):
		super().display()
		D.display(self)
		print("Hi from E") 	


class F(D): 
	def display(self):
		super().display()
		print("Hi from F")
		

class G(D):
	def display(self):
		super().display()
		print("Hi from G")
		
		
print("***** General Class *****")
a = A()
a.display()

d = D()
d.display()

print("***** Single Inheritance *****")
b = B()
b.display()

print("***** Multilevel Inheritance *****")
c = C()
c.display()

print("***** Multiple Inheritance *****")
e = E()
e.display()

print("***** Hierarchical Inheritance *****")
f = F()
f.display()

g = G()
g.display()

