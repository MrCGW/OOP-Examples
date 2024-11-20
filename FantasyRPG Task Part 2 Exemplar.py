########
#
# A Character class example for a fantasy RPG game.
# Version 2 - adding functionality to the attack method
#
########

import random

class Character():
    def __init__(self, name, race, char_class, health, strength):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.health = health
        self.strength = min(strength, 11) #Returns the smallest value, but caps at 11.

    def basic_information(self):
        print(f"{self.name} is a {self.race} {self.char_class} with {self.health} health and a strength of {self.strength}")

    def attack(self):
        roll = random.randint(1,6) + random.randint(1,6) #simulate 2 six sided dice roll
        print(roll) #Print result for testing
        return roll < self.strength #returns the roll value only if less than strength

    def damage(self):
        #Reduce health by 1. If health is less than 0, set it to 0.
        self.health -= 1
        if self.health < 0:
            self.health = 0
        return self.health

    def rest(self):
        self.health = min(self.health +5, 20) #add 5 to health to a maximum of 20
        print(f"Rested, health is now at {self.health}")

# Instantiate 3 objects

Hero = Character("Fernado", "Human", "Fighter", 18, 12) # Checks the min(strength) attribute. 12 will be changed to 11.
NME1 = Character("Fingle", "Ogre", "Barbarian", 20, 11)
NME2 = Character("Elvira", "Human", "Necromancer", 15, 9)

# Run the basic information method for each character instance

NME2.basic_information()
NME1.basic_information()
Hero.basic_information()

# Simple fight functionality - loops until hero health is 0
while Hero.health > 0:
    '''if Hero.attack():
        print(f"Hero has hit")
    else:
        print("Hero missed")'''

    if NME1.attack():
        print(f"{NME1.name} hit")
        print(f"{Hero.name}'s health is now {Hero.damage()}")
    else:
        print(f"{NME1.name} missed")

    if NME2.attack():
        print(f"{NME2.name} hit")
        print(f"{Hero.name}'s health is now {Hero.damage()}")
    else:
        print(f"{NME2.name} missed")
print(f"\n{Hero.name} died - game over!")