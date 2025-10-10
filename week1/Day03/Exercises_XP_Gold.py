#Ex01:

class Circle:
    def __init__(self,radius = 1.0):
        self.radius = radius
    def perimeter(self):
        P = self.radius * 2 * 3.14
        return P
    def area(self):
        A =3.14 * self.radius * self.radius
        return A
