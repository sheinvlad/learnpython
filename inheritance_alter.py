#inheritance alter

class Parent(object):
    def alter(self):
        print("PARENT alter")
		
class Child(Parent):
    def alter(self):
        print("Child alter before parent")
        super(Child, self).alter()
        print("Child after parent alter")

dad = Parent()
son = Child()

dad.alter()
son.alter()