class Car():
    def __init__(self, colour, speed):
        self.colour = colour
        self.speed = speed

    def rounded(self, speed): #A method to round speed divided by 7. NOT NECESSARILY GOOD PRACTICE
        return round(speed)

    def drive_forward(self):
        print(f"The {self.colour} car is driving forward at {self.speed} kph.")

    def reverse(self):
        reverse_speed = self.rounded(self.speed/7) #Illustration of calling another method in the class
        print(f"The {self.colour} car is reversing at {reverse_speed} kph.")

redCar = Car('Red', 50)
greenCar = Car('Green', 100)
redCar.drive_forward()
greenCar.reverse()
