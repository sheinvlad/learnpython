#composition
class Other(object):
    def override(self):
        print("Other override")
    def implicit(self):
        print("Other implicit")
    def alter(self):
        print("Other alter")
        
class Child(object):
    def __init__(self):
        self.other = Other()
    
    def override(self):
        print("Child override")
        
    def implicit(self):
        self.other.implicit()
    
    def alter(self):
        print("Child before Other alter")
        self.other.alter()
        print("Child after Other alter")
    

son = Child()

son.implicit()
son.override()
son.alter()
    
        