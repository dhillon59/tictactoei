import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getmove(self, game):
        pass

class Computer:
    def __init__(self, letter):
        super().__init__(letter)
        
    def getmove(self, game):
        square = random.choice(game.availablemoves())
        return square

class Gamer:
    def __init__(self, letter):
        super().__init__(letter)

    def getmove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + "input one through 9 spot: ")
            try: 
                val = int(square)
                if val not in game.availablemoves():
                    raise ValueError
            except ValueError:
                print('Invalid square, try again')
            
        return val