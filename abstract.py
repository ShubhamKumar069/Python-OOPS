from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Helloo")
        pass

class Dog(Animal):
    def sound(self):
        return "Bark!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())
