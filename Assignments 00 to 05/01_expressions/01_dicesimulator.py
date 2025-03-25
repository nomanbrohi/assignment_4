#import random from that you'll get the random function in your program
import random

#create two variable roll_side and roll number, roll side define the side of the dice is 6 and roll number mean the count of the dice
roll_side: int  = 6
roll_number: int = 0

#create a function to dice the roll
def roll_dice():

    #getting random number in dice1 and dice 2
    dice1 = random.randint(1,roll_side)
    dice2 = random.randint(1,roll_side)
    return dice1, dice2

#create another function for roll result and took two parameters dice1 and dice2 they are getting value form below d1 and d2
def roll_result(dice1, dice2):
    total = dice1 + dice2
    print(f"Roll {roll_number}: Die 1 = {dice1}, Die 2 = {dice2}, Total = {total}")


for i in range(1,4):
    #destructing the roll dice fucntion taking value in d1 and d2
    d1, d2 = roll_dice()
    roll_number += 1

    #giving d1 and d2 value to the argumnet in roll_result function 
    roll_result(d1, d2)


