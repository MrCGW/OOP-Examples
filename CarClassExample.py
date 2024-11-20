class car():
    def __init__(self, colour, speed):
        self.colour = colour
        self.speed = speed

    def rounded(self, speed):
        return round(speed)

    def drive_forward(self):
        print(f"The {self.colour} car is driving forward at {self.speed}.")

    def reverse(self):
        reverse_speed = self.rounded(self.speed/7)
        print(f"The {self.colour} car is reversing at {reverse_speed} kph.")

redCar = car('Red', 50)
greenCar = car('Green', 100)
redCar.drive_forward()
greenCar.reverse()
