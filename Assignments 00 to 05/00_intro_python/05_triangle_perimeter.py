def main():
    bold_italic = "\033[1;3m"
    reset = "\033[0m"

    side_1: float = float(input('What is the Length of side 1? '))
    side_2: float = float(input('What is the Length of side 2? '))
    side_3: float = float(input('What is the Length of side 3? '))

    total = side_1 + side_2 + side_3
    print(f'What is the length of side1? {bold_italic}{side_1}{reset}')
    print(f'What is the length of side2? {bold_italic}{side_2}{reset}')
    print(f'What is the length of side3? {bold_italic}{side_3}{reset}')
    print(f'The perimeter of the triangle is {total:.1f}')

if __name__ == "__main__":
    main()