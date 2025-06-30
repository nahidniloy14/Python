""""""

"""
A method is a function inside a class
"""

class Dog:
    species = "mammal"

    def __init__(self, name, breed, spots):
        self.name = name
        self.breed = breed
        self.spots = spots

    #Class Object Method

    """
    def bark(self):
    print("vau vau , My name is {}")
    """
    def bark(self,number):
        print("vau vau , My name is {}".format(self.name))
        print("My number is",+number)


    """
    def bark(self,number=19):
    print("vau vau , My name is {}".format(self.name))
    print("My number is",+number)
    """


person = Dog(name="Nazim", breed="neri", spots=False)
print(person.name)
print(person.breed)
print(person.spots)
print(person.species)

person.bark(19)

"""
Nazim
neri
False
mammal
vau vau
"""
"""
vau vau , My name is Nazim
My number is 19
"""

