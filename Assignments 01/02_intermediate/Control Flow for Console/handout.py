import random

def main():
    total_rounds = 1
    score = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    while total_rounds <= 5:
        print(f'\nRound {total_rounds}')

        computer_number = random.randint(1, 100)
        user_number = random.randint(1,100)

        print(f"Your number is {user_number}")
        
        user_choice = input("Do you think your number is higher(h) or lower(l) than the computer's? type h or l: ").strip().lower()
        if (user_choice == "h" and user_number > computer_number) or (user_choice == "l" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        total_rounds += 1
        print(f"Your score is now {score}")
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()