"""
Create a class Person with attributes name and age. Create an object and display its details.

Input: Person("Alice", 25)

Output: Name: Alice, Age: 25
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
p = Person("Alice", 25)

# Display details
p.display()