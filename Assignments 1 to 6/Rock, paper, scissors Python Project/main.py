#Rock, paper & scissors Python Project
#Import random for random choice

import random

def playGames():
    print("""\nWelcome to Rock Paper and Scissor Game You have 7 attempts """)

    choices = {'r':"Rock", 'p':"Paper", 's':"Scissor"}
    attempts = 7
    computer_score = 0
    user_score = 0

    while attempts > 0:

        computerChoice = random.choice(list(choices.values()))

        print(f'\nAttempts left = {attempts}')
        print(f'User Score = {user_score} Computer Score = {computer_score}')

        userInput = input("Please Choose 'R' Rock 'P' Paper 'S' Scissors: ").lower()

        if userInput not in choices:
            print("Invalid Entry Please use Correct word R P or S")
            continue
        userChoice = choices[userInput]

        if(userChoice == 'Rock' and computerChoice == 'Paper') or (userChoice == 'Paper' and computerChoice == 'Scissor') or (userChoice == 'Scissor' and computerChoice == 'Rock') :
            print(f'You lost! You chose {userChoice} and Computer chose {computerChoice}')
            computer_score += 1

        elif(userChoice == 'Paper' and computerChoice == 'Rock') or (userChoice == 'Scissor' and computerChoice == 'Paper') or (userChoice == 'Rock' and computerChoice == 'Scissor') :
            print(f'You won! You chose {userChoice} and Computer chose {computerChoice}')
            user_score += 1
        else:
            print(f'It\'s a tie You chose {userChoice} Computer chose {computerChoice} ')

        attempts -= 1

    print("\nGame Over")
    print(f'Your Score is {user_score} and computer Score is {computer_score}')

    if user_score > computer_score:
        print('Congratulations You won! the Game')
    elif user_score < computer_score:
        print('You lost! the Game')
    else:
        print("it's a draw")

playGames()