BOLD_ITALIC= "\033[1;3m"
RESET = "\033[0m"

def main():
    adjective:str = input("Please type an adjective and press enter. ") 
    noun:str = input("Please type an noun and press enter. ") 
    verb:str = input("Please type an verb and press enter. ") 

    print("Code in Place is fun. I learned to program and used Python to make my"+ " " + adjective + " " + noun + " " + verb + "!")

if __name__ == "__main__":
    main()