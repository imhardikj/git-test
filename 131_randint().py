from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        message = randint(1, self.sides)
        print(message)

my_die = Die(5)
my_die.roll_die()

my_die = Die(10)
my_die.roll_die()

my_die = Die(20)
my_die.roll_die()    
