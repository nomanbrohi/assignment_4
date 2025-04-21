# HangMan Python Project
import random
from words import word_list

def hangMan():

    attempts = 3
    print(f'\n🚀 You have total {attempts} attempts complete your word without loosing your life\n')

    random_word = random.choice(word_list).lower()
    word_length = len(random_word)
    guessed_letters = set()
    guessed_word_inList = ['-'] * word_length

    while attempts > 0:

        print(f"\n {' '.join(guessed_word_inList)}")

        userInput = input('Guess the correct word = ')

        if len(userInput) != 1 or not userInput.isalpha():
            print('\n⚠ invalid Character Please enter a valid character')
            continue

        if userInput not in random_word:
            attempts -= 1
            print(f'\n❌ wrong word you have only {attempts} attempts left')

        if userInput in guessed_letters:
            print('\n⚠ You already guessed this letter. Please try another one')
            continue

        guessed_letters.add(userInput)

        if userInput in random_word:
            for i in range(word_length):
                if userInput == random_word[i]:
                    guessed_word_inList[i] = userInput

            print("✅ Correct! " + userInput + " is in the word")

        if "-" not in guessed_word_inList:
            print(f'\n🎉 Congratulations! You have guessed the correct word {random_word}')
            break
    else:
        print("\n💀 Game Over! The correct word was:", random_word)
hangMan()