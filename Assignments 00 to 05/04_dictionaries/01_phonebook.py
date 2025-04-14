def get_contact():

    phoneBook = {}

    while True:
        name = input("Enter Name: ")
        if name.strip() == "":
            break
        
        number = input("Enter Number: ")
        if number.strip() == "":
            break
        num = int(number)

        phoneBook[name] = num

    return phoneBook

def lookup(phonebook):
    
    while True:
        name = input("Enter name for lookup: ")
        if name == '':
            break
        if name not in phonebook:
            print(f'{name} is not in the book')
        else:
            print(phonebook[name])

def print_phoneBook(phonebook):
    for contact in phonebook:
        print(f"Name: {contact} Phone Number: {phonebook[contact]}")


def main():
    phonebook = get_contact()
    print_phoneBook(phonebook)
    lookup(phonebook)


if __name__ == "__main__":
    main()