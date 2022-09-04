#inheritance override

#declare parent class
class Parent(object):
	def override(self):
		print("PARENT override()")

#declare inherited child class
class Child(Parent):
	def override(self):
		print("CHILD override()")
        
#create parent and class objects
dad = Parent()
son = Child()

#call override fucntion for both
dad.override()
son.override()