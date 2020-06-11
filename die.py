from random import randint

class Die():
    """A class to model a die"""

    def __init__(self, sides=6):
        """Assume a six-sided die"""
        self.sides = sides

    def roll(self):
        """Rolls the die and returns a number"""
        result = randint(1, self.sides)
        return result
