import random


class Dice:
    def roll(self):
        # return random integer [1, 6]
        return random.randint(1, 7)
    
class DiceProbability:
    def __init__(self, N) -> None:
        """_summary_

        Args:
            N (int): # of trial 
        """
        self.N = N
        self.a = [0] * N
        self.b = [0] * N
        # count result of Dice.roll
        # declare self.a
        
        # probability calculated by DiceProbability.calcProbability
        # declare self.b
    
    def calcProbability(self):
        dice = Dice()
        
        # As all values of self.a must be ZERO, initializing
        for i in range(6):
            self.a.append(dice.roll())
        
        # roll dice N times
        for i in range(6):
           self.b[i] = self.a.count(i + 1) / self.N
        
    def printProbability(self):
        for i, v in enumerate(self.b):
            print(f"{i + 1} probabilityss : {v:.2f}")