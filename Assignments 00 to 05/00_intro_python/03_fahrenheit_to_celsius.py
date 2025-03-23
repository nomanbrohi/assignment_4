def main():
    try:
        user_input : float = float(input('Enter Temperature in Fahrenheit: '))
        bold_italic = "\033[1;3m"
        reset = "\033[0m"

        celsius = (user_input - 32) * 5.0/9.0

        return (f'Temperature: {bold_italic}{user_input}{reset}F = {celsius:.2f}C')
    except:
        return ('Invalid input Enter numbers only')

main = main()
if __name__ == '__main__':
    print(main)