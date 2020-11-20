class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def surface(self):
        return self.length * self.surface()

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width
