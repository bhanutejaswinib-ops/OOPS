class animal:
    def eat(self):
        print("animal eat food")
class Dog(animal):
    def speak(self):
        print("dog bark")
d1=Dog()
d1.eat()
d1.speak()