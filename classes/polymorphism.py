class Shape():
    def __init__(name):
        self.name = name
        

    def area(self):
        return self.l * self.w






class Triangle(Shape):
    super(). __init__(self, l, w, h):
        self.l = l
        self.h = h
        self.w = w

    def area(self):
        return 0.5 * self.base * self.height