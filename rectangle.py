from math import pi


class figure:
    def __init__(self, name):
        self.name = name
        self.area = 0

    def print_area(self):
        print("{} area = {}".format(self.name, self.area))


class rectangle(figure):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
        figure.__init__(self, "Rectangle")

    def calculate_area(self):
        self.area = self.len * self.wid

    def print_area(self):
        self.calculate_area()
        figure.print_area(self)


class circle(figure):
    def __init__(self, radius):
        self.radius = radius
        figure.__init__(self, "Circle")

    def print_area(self):
        calc = lambda r: pi * (r * r)
        self.area = calc(self.radius)
        figure.print_area(self)


newFigure = figure("New figure")
newFigure.area = 58
newRectangle = rectangle(5, 4)
newCircle = circle(10)

newFigure.print_area()
newRectangle.print_area()
newCircle.print_area()
