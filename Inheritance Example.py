class Animal():
    def __init__(self, name, colour, eye_colour, height, length, weight, sound):
        self.name = name
        self.colour = colour
        self.eye_colour = eye_colour
        self.height = height
        self.length = length
        self.weight = weight
        self.sound = sound

    def info(self):
        thing = type(self).__name__ # stores the class name in the variable 'thing'
        print(f"{self.name} is a {self.colour} {thing.lower()} that is {self.height} cm high, {self.length} cm long, weighs {self.weight}, and has {self.eye_colour} eyes.")
    def make_sound(self):
        print(f"{self.name}'s sound: {self.sound}")
    def eat(self):
        print ("eating")
    def drink(self):
        print("drinking")
    def sleep(self):
        print("sleeping")

class Dog(Animal): #A child class, inherits attributes and methods

    def wag_tail(self): #method specific to the Dog class.
        print("Tail wagging...")

class Cat(Animal): #A child class, inherits attributes and methods

    def roam(self): #method specific to the Cat class.
        print("Roaming...")

Archie = Cat('Archie', 'ginger', 'brown', 30, 50, 5, 'meow')
Rover = Dog('Rover','black', 'blue', 50, 75, 10, 'woof')

Archie.info()
Archie.make_sound()
Archie.roam()
Rover.info()
Rover.make_sound()
Rover.wag_tail()