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
#Ex02 :

class MyList :
    def __init__(self,letters):
        self.letters = letters
    def rev_list(self):
        self.letters.reverse()
        print(self.letters)
    def sort_list(self):
        return sorted(self.letters)

#Ex03 :
