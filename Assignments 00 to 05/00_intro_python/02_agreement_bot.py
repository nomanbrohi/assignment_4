def main():
    user_input: str = input("What's your favorite animal? ")
    bold_italic = "\033[1;3m"
    reset = "\033[0m"

    print(f'My favorite animal is also {bold_italic}{user_input}{reset}!')

if __name__ == "__main__":
    main()