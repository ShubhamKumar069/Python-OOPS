class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getage(self):
        return self.__age

tim = Dog("Jim", 20)
print(tim.getage())