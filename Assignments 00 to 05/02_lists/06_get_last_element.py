
bold_italic = "\033[1;3m"
reset = "\033[0m"

def get_last_element(lst):
    if lst:
        lst_len = len(lst)
        print(lst[lst_len-1])

def main():
    lst = []
    user_input = input(f"Enter Element (or Enter to quit): {bold_italic}")
    print(reset, end='')

    while user_input != "":
        lst.append(user_input)
        user_input = input(f"Enter Element (or Enter to quit): {bold_italic}")
        print(reset, end='')
    if lst:
        get_last_element(lst)

main()