class _Private(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

class NotPrivate(object):
    def sayhello(self):
        print("Hello")

tim = NotPrivate()
tim.sayhello()