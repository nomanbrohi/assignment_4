# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

peturksbouipo = 16
stanlau = 25
mayengua = 48

blue = '\033[94m'
reset = '\033[0m'

def main():
    try:
        user_age = int(input(f'How old are you? {blue}'))
        print(reset, end='')
        
        # Check voting eligibility for each country
        if user_age >= peturksbouipo:
            print(f"- You CAN vote in Peturksbouipo (voting age: {peturksbouipo})")
        else:
            print(f"- You CANNOT vote in Peturksbouipo (voting age: {peturksbouipo})")
            
        if user_age >= stanlau:
            print(f"- You CAN vote in Stanlau (voting age: {stanlau})")
        else:
            print(f"- You CANNOT vote in Stanlau (voting age: {stanlau})")
            
        if user_age >= mayengua:
            print(f"- You CAN vote in Mayengua (voting age: {mayengua})")
        else:
            print(f"- You CANNOT vote in Mayengua (voting age: {mayengua})")
            
    except ValueError:
        print(reset,end='')
        print("Please enter a valid age as a number.")

if __name__ == "__main__":
    main()