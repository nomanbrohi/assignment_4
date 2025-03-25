
#import math library to use the sqrt function
import math

#(BC = √(AB² + AC²)
#creating bold italic variable  and reset
bold_italic = "\033[1;3m"
reset = "\033[0m"

def main():
    
    #get user input for AB Value
    ab: float = float(input(f"Enter the length of AB: {bold_italic}"))
     #reset the bold italic otherwise it'll convert whole program in bold italic
    print(reset, end='')

    #get user input for AC Value
    ac: float = float(input(f"Enter the length of AC: {bold_italic}"))
     #reset the bold italic otherwise it'll convert whole program in bold italic
    print(reset, end='')

    #calculate it to get the lenght of BC 
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f'The length of BC is: {bold_italic}{bc}{reset}')

main()
