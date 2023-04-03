import math


class Shape:
    shape_name = "shape"

    def __init__(self):
        pass

    def get_area(self):
        pass

    def __str__(self):
        return f"This shape is a {self.shape_name}"


class Rectangle(Shape):
    shape_name = "rectangle"

    def __init__(self, width=0, height=0):
        if width > 0:
            self._width = width
        else:
            self._width = 1
        if height > 0:
            self._height = height
        else:
            self._height = 1

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width >= 1:
            self._width = width
        else:
            self._width = 1

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height >= 1:
            self._height = height
        else:
            self._width = 1

    def get_area(self):
        return self._width * self._height


class Square(Rectangle):
    shape_name = "square"

    def __init__(self, side):
        if side > 0:
            super().__init__(side, side)
        else:
            super().__init__(1, 1)

    def get_side(self):
        return self._width

    def set_side(self, side):
        if side >= 1:
            self._width = side
            self._height = side
        else:
            self._width = 1
            self._height = 1


class Circle(Shape):
    shape_name = "circle"

    def __init__(self, radius):
        if radius >= 1:
            self._radius = radius
        else:
            self._radius = 1

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        if radius >= 1:
            self._radius = radius
        else:
            self._radius = 1

    def get_area(self):
        return (self._radius ** 2) * math.pi


def main():
    my_rect = Rectangle(10, 5)
    my_square = Square(6)
    my_circle = Circle(3)

    shapes = [my_rect, my_square, my_circle]
    for shape in shapes:
        print(shape)

    print()

    for shape in shapes:
        print(f"The area of the {shape.shape_name} is: {shape.get_area()}")


if __name__ == '__main__':
    main()
