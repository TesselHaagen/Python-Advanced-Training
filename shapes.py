
class Shape():
    pi = 3.14159
    def __init__(self, w):
        self.w = w
        self.perimeter = 0
        self.surface = 0
    
    def __str__(self):
        return f"This is a shape with a perimeter of {round(self.perimeter, 2)} and a surface of {self.surface}"

    def __eq__(self, other):
        return self.perimeter == other.perimeter
        # return self.surface == other.surface
        # return self.perimeter == other.perimeter and self.surface == other.surface

    def __lt__(self, other):
        return self.perimeter < other.perimeter
    
class Circle(Shape):
    def __init__(self, w):
        super().__init__(w)
        self.perimeter = self.calc_perimeter()
        self.surface = self.calc_surface()
    
    def calc_perimeter(self):
        return self.w*self.pi


    def calc_surface(self):
        return (self.w/2)**2*self.pi

class Square(Shape):
    def __init__(self, w):
        super().__init__(w)
        self.perimeter = self.calc_perimeter()
        self.surface = self.calc_surface()
    
    def calc_perimeter(self):
        return self.w*4

    def calc_surface(self):
        return self.w**2


circ = Circle(10)
square = Square(10)
print(circ)
print(square)
print(circ == square) # circ.__eq__(square)
print(circ < square) # circ.__lt__(square)
print(square < circ) # square.__lt__(circ)