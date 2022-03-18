#getString printString

class getString:
    
    def __init__(self, s):
        self.s = s
        
    def printString(self):
        print(self.s)
        
first = getString("Hello World!")
first.printString()