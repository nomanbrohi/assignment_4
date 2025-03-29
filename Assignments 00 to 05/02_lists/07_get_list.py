blue = "\033[94m"
reset = "\033[0m"

def list():
    lst = []

    user_input = input(f'Enter Element for list: {blue}').strip()
    print(reset, end='')
    while user_input != "":
        lst.append(user_input)
        user_input = input(f'Enter Element for list: ')
        if user_input == "":
            break
    if lst:
        print(lst)
    

list()