#import the random library to get some random function
import random

#number of sides of each die
dice_sides: int = 6

def main():
    #get random number for dice 1
    dice_1: int = random.randint(1,dice_sides)

    #get random number for dice 2 
    dice_2: int = random.randint(1,dice_sides)

    #calculate the random number of both dice
    total: int = dice_1 + dice_2

    print(f'Dice 1: {dice_1}\nDice 2: {dice_2}\nTotal of two dice: {total}')

main()