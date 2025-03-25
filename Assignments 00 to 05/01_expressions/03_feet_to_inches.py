
#constant value of inches in 1 foot
inches_in_foot: int = 12

#creating bold italic variable  and reset
bold_italic = "\033[1;3m"
reset = "\033[0m"

def main():
    #user input in foot 
    feet :float = float(input(f"Enter value in Foot: {bold_italic}"))
    #reset the bold italic otherwise it'll convert whole program in bold italic
    print(reset, end='')

    #calculate the feet in to inches
    result = feet * inches_in_foot

    print(f'{bold_italic}{feet}{reset} Feet equal to {bold_italic}{result}{reset} Inches')

main()