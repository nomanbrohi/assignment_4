
def add_three_copies(list, data):
    for i in range(3):
        list.append(data)

def main():
    user_input = input("Enter a Message to Copy: ")
    list = []
    add_three_copies(list, user_input)
    print(list)

if __name__ == "__main__":
    main()