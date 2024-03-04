"""Rectangle"""


class Rectangle:
    """Square and perimeter rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        """Square rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter rectangle"""
        return 2 * self.height + 2 * self.width


rect = Rectangle(2, 4)
square = rect.square()
perimeter = rect.perimeter()

print(square, perimeter)
