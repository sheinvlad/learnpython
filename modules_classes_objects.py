#modules classes and objects
class MyStuff(object):
    def __init__(self):
        self.tangerine = "Some tngrn"
    
    def apple(self):
        print("My apple")
    
        
thing = MyStuff()
thing.apple()
print(thing.tangerine)
