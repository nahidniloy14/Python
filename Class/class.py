"""
Class
"""

"""
Use Camel Casing to name a class
CamelCasing
"""


class Sample():
    pass


# Instance of a class
my_sample = Sample()
print(type(my_sample))


class Point:
    def move(self):  # method
        print("move")

    def draw(self):
        print("draw")


# object creation of class
shape = Point()
shape.draw()
shape.x = 10
print(shape.x)
