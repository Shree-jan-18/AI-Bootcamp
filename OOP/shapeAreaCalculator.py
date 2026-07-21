class Shape:
    def area(self):
        print("Area cannot be calculated.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle: ", self.length * self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle: ", 3.14 * self.radius * self.radius)

#Creating objects of Rectangle and Circle classes
rectangle = Rectangle(5, 4)
circle = Circle(3)

#Polymorphism: Calling the area method of both classes
rectangle.area()
circle.area()