########
#
# A Character class example for a fantasy RPG game.
# Version 1 - setting up attributes, creating the basic information method.
# Adding placeholder methods for attack, damage, and rest
#
########

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
        pass # pass allows the method to exist without doing anything.

    def damage(self):
        pass

    def rest(self):
        pass

# Instantiate 3 objects

Hero = Character("Fernado", "Human", "Fighter", 18, 12) # Checks the min(strength) attribute. 12 will be changed to 11.
NME1 = Character("Fingle", "Ogre", "Barbarian", 20, 11)
NME2 = Character("Elvira", "Human", "Necromancer", 15, 9)

# Run the basic information method for each character instance

NME2.basic_information()
NME1.basic_information()
Hero.basic_information()
