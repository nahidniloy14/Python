class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


my_animal = Animal()
my_animal.eat()


class Dog(Animal):

    def __init__(self):
        # create an instance of animal class
        Animal.__init__(self)
        print("Dog Created")

    def eat(self):
        print("I eat pedigree")

    def bark(self):
        print("Woof wwooof woowwoof")



my_dog = Dog()
print(my_dog.eat())
print(my_dog.bark())
