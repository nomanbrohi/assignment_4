import random

start_num: int = 0
end_num: int = 20
random_number: int = random.randint(start_num, end_num)

def guess_number():
    print(f"I am thinking of a number between {start_num} and {end_num}...")
    
    while True:
        try:
            user_guess = int(input("Enter a guess: "))
            
            if user_guess < random_number:
                print("Your guess is too low\n")
            elif user_guess > random_number:
                print("Your guess is too high\n")
            else:
                print(f"🎉 Congrats! The number was: {random_number}")
                break
        
        except ValueError:
            print("❗ Please enter a valid number!\n")

guess_number()
