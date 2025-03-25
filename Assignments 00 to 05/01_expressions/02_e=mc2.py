#constant value of light
c: int = 299792458

#creating bold italic variable  and reset
bold_italic = "\033[1;3m"
reset = "\033[0m"

def main():
    #input mass in kg from user
    mass: float = float(input(f"Enter Kilos of mass: {bold_italic}"))
    #reset the bold italic otherwise it'll convert whole program in bold italic
    print(reset, end='')

    print(f'm = {mass} kg')
    print(f'C = {c} m/s')
    print("Formula to find the Energy of joules 'e = m * c**2'")
    print(f'e = {mass}({c}^2)')
    e = mass * (c**2)
    result = f'Value of E = {bold_italic}{e}{reset}'

    return result

result = main()
print(result)