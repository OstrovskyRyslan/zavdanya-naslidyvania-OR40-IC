class Shape:
    def __init__(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def area(self):
        import math
        return math.pi * self.__radius ** 2
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    def get_height(self):
        return self.__height
    def set_height(self, height):
        self.__height = height
    def area(self):
        return self.__width * self.__height
circle = Circle("Red", 5)  
rectangle = Rectangle("Blue", 4, 6)  
print(f"Площа кола: {circle.area():.2f}")
print(f"Площа прямокутника: {rectangle.area()}")
