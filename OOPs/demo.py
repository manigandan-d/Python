# class name should be in PascalCase

class Demo: # Demo - class - template for the object - blueprint
	z = 122 # class attribute 
	
	# instance attribute - object has - properties - state - data member 
	
	def __init__(self, a, ch): 
		self.a = a
		self.ch = ch
		# self.z = 122
		
	# method - object does - behaviour - member function 
	
	def display(self): 
		print("method")
	


# object instantiation 

d1 = Demo(5, 'A') # d1 - object - instance of the class - identity - name of the object 

print(d1.a, d1.ch, d1.z)

d2 = Demo(10, 'B')

print(d2.a, d2.ch, d2.z)

