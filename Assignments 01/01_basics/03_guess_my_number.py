import random 


def main():
    random_num = random.randint(1,99)
    print("I am thinking of a number between 1 and 99...")
    while True:
        print(random_num)
        user_guess = int(input("Enter a guess: "))
        if user_guess < random_num:
            print("your guess is low")
        elif user_guess > random_num:
            print("your guess are high")
        else:
            print("Congrats you guess the correct number")
            break

if __name__ == "__main__":
    main()