max_length: int = 3
bold_italic = '\033[1;3m'
reset = '\033[0m'

def shorten_lst(lst):
    while len(lst) != max_length:
        item_removed = lst.pop()
        print(item_removed)
    print(f'final list {lst}')

def get_list():

    lst = []
    user_input = input(f"Enter an Element for your List:{bold_italic} ")
    print(reset, end='')
    while True:
        if user_input != '':
            lst.append(user_input)
            user_input = input(f"Enter an Element for your List:{bold_italic} ")
            print(reset, end='')
        else:
            break
    shorten_lst(lst)

get_list()
