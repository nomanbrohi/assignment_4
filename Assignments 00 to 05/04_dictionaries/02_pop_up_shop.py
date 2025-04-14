# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5

bold_italic = '\033[1;3m'
reset = '\033[0m'

def main():
    fruits = {'apple': 1.5, 'durian': 2, 'jackfruit': 5, 'kiwi': 3, 'rambutan': 7, 'mango': 10}
    total_cost = 0
    try:
        for fruit in fruits:
            price = fruits[fruit]
            quantity = int(input(f'How many ({fruit}) do you want?:{bold_italic} '))
            print(reset, end='')
            total_cost += (price * quantity)
        print(f'Total Cost of fruits ${str(total_cost)}')
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()