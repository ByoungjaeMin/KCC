from dice import DiceProbability

def main():
    N = int(input("Total Trials : "))
    dice_probabilty = DiceProbability(N)
    dice_probabilty.calcProbability()
    dice_probabilty.printProbability()

if __name__ == "__main__":
    main()