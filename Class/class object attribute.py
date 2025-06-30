class Dog:
    # Class Object Attribute
    species = "mammal"

    def __init__(self, name, breed, spots):
        self.name = name
        self.breed = breed
        self.spots = spots


person = Dog(name="Nazim", breed="neri", spots=False)
print(person.name)
print(person.breed)
print(person.spots)
print(person.species)
"""
Nazim
neri
False
mammal
"""


