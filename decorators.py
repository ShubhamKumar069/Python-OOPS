class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod #Decorator
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod #Decorator
    def bark(n):
        print("Bark!")

    def __repr__(self):
        return f"Dog({self.name})"



print(Dog.dogs)
print(Dog.num_dogs())