mix_list = ["apple", "orange", "python", "typescript", "nextjs"]

def main():
    menu = ['accessing', 'modifying', 'slicing']
    action = {1: access, 2:modify, 3: slice}
    
    print("What do you want to do?")

    for index, q in enumerate(menu):
        print(f'{index+1}: {q.title()}')

    user_prompt = input("Enter the number (1, 2, or 3): ")
    
    if user_prompt.isdigit():
        choice = int(user_prompt)
        if 1 <= choice <= len(menu):
            print(f"You chose: {menu[choice - 1].title()}")
            if choice in action:
                action[choice]()

        else:
            print("Invalid number. Please choose between 1 and 3.")
    else:
        print("Please enter a valid number.")

def access():
    user_input = int(input("Enter number to select element: "))
    if user_input < 1 or user_input >= len(mix_list):
        print("Invalid Number! Please choose between 1 and 5.")
    else:
        print(f'- {mix_list[user_input].title()}')

def modify():
    user_input = int(input("Enter Index to replace: "))
    if user_input > len(mix_list) or user_input < 1:
        print("Invalid Number! Please choose between 1 and 5.")
    else:
        replace_e = input("Enter Element: ")
        mix_list[user_input-1] = replace_e
        print(mix_list)

def slice():
    print(mix_list)
    start_index = int(input("Enter the start number: "))
    end_index = int(input("Enter the end number: "))
    if start_index < 1 or start_index > 5:
        print("Invalid start number Please choose between 1 and 5.")
    elif end_index > 5:
        print("Invalid end number Please choose between 1 and 3.")
    else:    
        new_list = mix_list[start_index-1:end_index-1]
        print(new_list)

if __name__ == "__main__":
    main()