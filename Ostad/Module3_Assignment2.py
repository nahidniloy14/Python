"""
Create a base class Animal and a derived class Dog that inherits from Animal.

Output:

Animals make different sounds. # From Animal class

Dog barks! # From Dog Class
"""

# Base class
class Animal:
    def make_sound(self):
        print("Animals make different sounds.")  # From Animal class

# Derived class
class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Call the base class method
        print("Dog barks!")  # From Dog class

# Create an instance of Dog
d = Dog()
d.make_sound()
