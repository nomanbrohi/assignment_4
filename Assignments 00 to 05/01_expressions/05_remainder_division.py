
#creating bold italic variable  and reset
bold_italic = "\033[1;3m"
reset = "\033[0m"

def main():
    #get the dividend from the user
    num1:int= int(input(f"Please Enter the number to be divided: {bold_italic}"))
    #reset the bold italic otherwise it'll convert whole program in bold italic
    print(reset, end='')
    
    #get the divisor from the user
    num2:int= int(input(f"Please Enter the number to divided by: {bold_italic}"))
    #reset the bold italic otherwise it'll convert whole program in bold italic
    print(reset, end="")

    #calculate for remainder
    remainder = num1 % num2
    #calculate for division
    division = num1 / num2
    
    print(f"The result of {num1}/{num2} is {int(division)} with a remainder {remainder}")

main()