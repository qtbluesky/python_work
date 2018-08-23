from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print("Result: " + str(x))

my_die = Die(20)
my_die.roll_die()