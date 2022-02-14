class Rectangle: # ПРЯМОУГОЛЬНИК
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area_rectangle(self): # площадь прямоугольника
        return self.a * self.b
    def get_perimetr_rectangle(self): # периметр прямоугольника
        return (self.a + self.b) * 2

class Square: # КВАДРАТ
    def __init__(self, a):
        self.a = a
    def get_area_square(self): # площадь квадрата
        return self.a**2
    def get_perimetr_square(self): # периметр квадрата
        return self.a * 4

class Circle: # КРУГ
    def __init__(self, r, pi=3.14):
        self.r = r
        self.pi = pi
    def get_area_circle(self): # площадь круга
        return self.pi * self.r**2
    def get_circumference_length(self): # окружность
        return 2 * self.pi * self.r