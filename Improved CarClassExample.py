class Car:
    def __init__(self, colour: str, speed: float): #Clear definition of data types
        """Initialize the car with a colour and speed."""
        self.colour = colour
        self.speed = speed

    def drive_forward(self):
        """Print a message about the car driving forward."""
        print(f"The {self.colour} car is driving forward at {self.speed} kph.")

    def reverse(self):
        """Print a message about the car reversing at a reduced speed."""
        reverse_speed = round(self.speed / 7)  # Calculate reverse speed efficiently
        print(f"The {self.colour} car is reversing at {reverse_speed} kph.")


# Instantiate car objects
red_car = Car("Red", 50)
green_car = Car("Green", 100)

# Call methods
red_car.drive_forward()
green_car.reverse()