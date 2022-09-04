#inheritance implicit

#declare parent class
class Parent(object):
	def implicit(self):
		print("PARENT implicit()")

#declare inherited child class
class Child(Parent):
    pass
    
#create parent and class objects
dad = Parent()
son = Child()

#call implicit fucntion for both
dad.implicit()
son.implicit()

