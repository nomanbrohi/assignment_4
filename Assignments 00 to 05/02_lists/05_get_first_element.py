
bold_italic = "\033[1;3m"
reset = "\033[0m"

def get_first_element(lst):
    if lst:
        print(lst[0])

def main():
    lst = []
    user_input = input(f"Enter Element (or Enter to quit): {bold_italic}")
    print(reset, end='')

    while user_input != "":
        lst.append(user_input)
        user_input = input(f"Enter Element (or Enter to quit): {bold_italic}")
        print(reset, end='')
    if lst:
        get_first_element(lst)

main()