class cat(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name : ",self.name,", Age :",self.age)

    def meow(self):
        print(self.name, "Says Meow")

    def birthDay(self):
        self.age += 1
        print(self.name, "is now ",self.age)

    def info(self):
        print("Name:", self.name, ", Age:", self.age)

cat = cat("Dog", 7)
cat.meow()
cat.birthDay()
cat.info()