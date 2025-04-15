AFFIRMATION: str = "Do not Loose your hope you'll be success One Day"

def main():
    while True:
        prompt = input(f"\nPlease type the following affirmation: \n{AFFIRMATION}\n")
        if prompt.strip() == '':
            continue
        if prompt != AFFIRMATION:
            print("That was not the affirmation.")
        else:
            print("That's right! :)")
            break
if __name__ == "__main__":
    main()