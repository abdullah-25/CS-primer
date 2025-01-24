import math

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return f"({self.x}, {self.y})"
   
    def add(self, other):
        x = other.x + self.x
        y = other.y + self.y
        return Vector(x,y)
    
    def comparison(self, other):
        return self.x == other.x and self.y == other.y

    def magnetitude(self):
        a = self.x ** 2 + self.y ** 2
        return math.sqrt(a)


class displacement(Vector):
    def displacement(self, velocity, time):
        self.x = self.x * velocity * time
        self.y = self.y * velocity * time



if __name__ == '__main__':
    v1 = Vector(1,2)
    v2 = Vector(2,3)
    v3 = Vector(4,5)

    # Test addition
    v3 = v1.add(v2)  # Should be Vector(3,5)

    # Test comparison
    is_equal1 = v3.comparison(Vector(3,4))  # Should be False
    is_equal2 = v3.comparison(Vector(3,5))  # Should be True

    v5 = Vector(3,4)
    length = v5.magnetitude()  # Should be 5

    d = displacement(2,3)
    d.displacement(2,3)

    is_equal = d.comparison(Vector(3,5))

    print(v3.show())
    print(is_equal1, is_equal2, is_equal)
    print(length)
