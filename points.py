class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
        print("(", self.x , ",", self.y ,")")

    def move(self, x, y):
        self.x += x
        self.y += y
        print("(", self.x , ",", self.y ,")")
        self.coords = (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        return NotImplemented


p1 = Point(3, 4)
p2 = Point(3, 2)


p3 = p1 + p2
p4 = p1 - p2
p5 = p1 * p2
p6 = p1 / p2