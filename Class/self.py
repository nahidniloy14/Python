""""""
"""
__init__ method is called upon whenever we are making instance of a class
__init__ constructor for a class
self hepls to refer to itself
self represents the instance of an object itself
(self,breed) >> breed here is the argument
self.breed >> breed here is the attribute name
person = Human(name="Niloy")>> name will take value of the argumnet
print(person.name)>> person.attributename
"""


class Human():
    def __init__(self, name):
        self.name = name


person = Human(name="Niloy")
print(person.name)
