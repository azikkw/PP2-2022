#getString printString

class Shape:
    
    def __init__(self, area):
        self.area = area
        
class Square(Shape):
    
    def __init__(self, area):
        super().__init__(area)
        
    def __init__(self, a, area):
        self.a = a
        self.area = area
        
    def sq_area(self):
        area = self.a ** 2
        print(area)
        
eq = Square(4, 0)
eq.sq_area()