#area of Rectangle

class Shape:
    
    def __init__(self, area):
        self.area = area
        
class Rectangle(Shape):
    
    def __init__(self, area):
        super().__init__(area)
        
    def __init__(self, a, b, area):
        self.a = a
        self.b = b
        self.area = area
        
    def rec_area(self):
        area = (self.a * self.b) / 2
        print(area)
        
eq = Rectangle(4, 3, 0)
eq.rec_area()