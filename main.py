class Dog(object):
    def __init__(self, name):
        print("You made a Dog!") 
        self.name = name

    def speak(self):
        print("The Dog's name is :",self.name)

    def change_name(self, name):
        self.name = name
        print("Nahh your Dog's name is :",self.name)

Tim = Dog("Tim")
Tim.speak()
Tim.change_name("Ron")