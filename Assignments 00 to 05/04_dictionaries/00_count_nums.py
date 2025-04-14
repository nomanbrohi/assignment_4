# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def user_numbers():
    num_list = []
    while True:
        user_input = input("Enter Number: ")
        
        if user_input.strip() == "":
            print("Exit")
            break
        number = int(user_input)
        num_list.append(number)
    return num_list

def count(num_lst):

    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    for nums in num_dict:
        print(f"{str(nums)} appears {num_dict[nums]} times")
    
    

def main():
    count(user_numbers())

main()
