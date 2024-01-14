class A:
	def display(self):
		print("Hi from A")
		

class B(A):
	pass
	# def display(self):
	#	print("Hi from B")
		
		
class C(A):
	pass
	# def display(self):
	#	print("Hi from C")


class D(B, C):
	pass
	# def display(self):
	#	print("Hi from D")
		

d = D()

d.display()

print(D.mro())

