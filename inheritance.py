class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("My name is",self.name,"I am", self.age, "Years Old")

    def talk(self):
        print("Bark!")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("My name is",self.name,"I am", self.age, "Years Old and My color is",self.color)

    def talk(self):
        print("Meow!")
        

luna = Cat("Luna", 5, "Orange")
luna.speak()
luna.talk()

print(" ")

larry = Dog("Larry", 69)
larry.speak()
larry.talk()