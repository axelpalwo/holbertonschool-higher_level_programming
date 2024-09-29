from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        return

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())
