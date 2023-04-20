class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


my_dog = Dog("Niko")
my_cat = Cat("Felix")

print(my_cat.speak())
print(my_dog.speak())

for pet in [my_cat, my_dog]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())


print(pet_speak(my_dog))
print(pet_speak(my_cat))
