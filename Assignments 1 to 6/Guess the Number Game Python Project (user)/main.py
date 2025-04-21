#Guess the number game (User) where the computer has to guess the correct number.

def computerGuess(your_number):
    print(f'Think of the number from 1 to {your_number}')
    low = 1
    high = your_number
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"my guess is {guess}")
        user_Answer = input("Higher(h),Lower(l),or Correct(c): ").lower()
        if(user_Answer == "h"):
            print('your guess is low')
            low = guess + 1
        elif(user_Answer == "l"):
            print('your guess is high')
            high = guess - 1
        elif(user_Answer == 'c'):
            print(f"Huuurray you guess the correct number in {attempts} attempts")
            break

        print("something went Wrong... please restart")

computerGuess(10)