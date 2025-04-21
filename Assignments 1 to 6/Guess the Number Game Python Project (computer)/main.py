import random

def guess_the_number(a):
  secret_number = random.randint(1, a)
  while True:
    user_input = int(input("Please Enter Your Guess = "))

    if secret_number < user_input:
      print("Too low please try your luck again!!!")
    elif secret_number > user_input:
      print("Too High please try your luck again!!!")
    else:
      print(f"woohooo CONGRAGULATION you guess the correct number {secret_number}")
      break

guess_the_number(10)