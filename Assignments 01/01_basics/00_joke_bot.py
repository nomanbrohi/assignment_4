joke: str = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
prompt: str = "What do you want? "
sorry: str = "Sorry I only tell jokes"
blue = "\033[34m"
reset = "\033[0m"
def main():

    while True:
        user_input = input(f'{prompt}{blue}').strip().lower()
        print(reset, end='')

        if "joke" in user_input:
            print(f"Here is a joke for you! {joke}")
            break
        else:
            print(sorry)
            continue
    
if __name__ == "__main__":
    main()