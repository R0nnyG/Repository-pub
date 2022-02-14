from rectangle import Rectangle, Square, Circle
# создаем два прямоугольника
rect_1 = Rectangle(12, 5)
rect_2 = Rectangle(6, 8)
print("Площадь прямоугольника =",rect_1.get_area_rectangle(),
      "Периметр прямоугольника =", rect_1.get_perimetr_rectangle())
# создаем два квадрата
square_1 = Square(12)
square_2 = Square(6)
print("Площадь квадрата =", square_1.get_area_square(),
      "Периметр квадрата =", square_1.get_perimetr_square())
# создаем два круга
circle_1 = Circle(5)
circle_2 = Circle(10)
print("Площадь круга =", "{:8.4f}".format(circle_1.get_area_circle()),
      "Длина окружности =", "{:8.4f}".format(circle_1.get_circumference_length()))

print(""), print("-----===== Функция isinstance =====-----"), print("")

figures = [rect_1, square_1, circle_1, rect_2, square_2, circle_2]
for figure in figures:
    if isinstance(figure, Rectangle):
        print("Площадь прямоугольника =", figure.get_area_rectangle(),
              "Периметр прямоугольника =", figure.get_perimetr_rectangle())
    elif isinstance(figure, Square):
        print("Площадь квадрата =", figure.get_area_square(),
              "Периметр квадрата =", figure.get_perimetr_square())
    else:
        print("Площадь круга =", "{:8.4f}".format(figure.get_area_circle()),
              "Длина окружности =", "{:8.4f}".format(figure.get_circumference_length()))