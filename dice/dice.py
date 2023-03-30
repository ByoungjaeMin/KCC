import random


class Dice:
    def roll(self):
        # return random integer [1, 6]\
        return random.randint(1, 6)
    
class DiceProbability:
    def __init__(self, N) -> None:
        """_summary_

        Args:
            N (int): # of trial 
        """
        self.N = N
        self.a = [0] * 6
        self.b = [0] * 6
        # count result of Dice.roll
        # declare self.a
        
        # probability calculated by DiceProbability.calcProbability
        # declare self.b
    
    def calcProbability(self):
        dice = Dice()
        
        # As all values of self.a must be ZERO, initializing
        for i in range(self.N):
            self.a[dice.roll()-1] += 1
        
        # roll dice N times
        for i in range(6):
           self.b[i] = self.a[i] / self.N
        
    def printProbability(self):
        for i, v in enumerate(self.b):
            print(f"{i + 1} probabilityss : {v:.3f}")