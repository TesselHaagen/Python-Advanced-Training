class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    



v1 = Vector(3,3)
v2 = Vector(1,4)

print(v1) #v1.__str__()
v3 = v1 + v2 # v1.__add__(v2)
v4 = v1 - v2 # v1.__sub__(v2)
print(v1==v2) # v1.__eq__(v2)