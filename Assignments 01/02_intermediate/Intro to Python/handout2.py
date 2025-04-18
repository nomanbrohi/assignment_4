def main():
    print("Welcome to Planetary Weight Calculator")
    print("-------------------------------------")

    planets_gravity = {
        "mercury": 37.6,
        "venus": 88.9,
        "mars": 37.8,
        "jupiter": 236.0,
        "saturn": 108.1,
        "uranus": 81.5,
        "neptune": 114.0
    }

    user_weight_on_earth = float(input("Enter your weight on Earth (kg): "))
    print("\nSelect a planet:")

    planet_list = list(planets_gravity.keys())
    
    for index, planet in enumerate(planet_list, start=1):
        print(f'{index}: {planet.title()}')

    choice = int(input("Choose planet number (1 to 7): "))
    if 1 <= choice <= len(planet_list):
        selected_planet = planet_list[choice - 1]
        gravity = planets_gravity[selected_planet]/100
        weight_on_planet = round(user_weight_on_earth * gravity, 2) 
        print(f"\nYour weight on {selected_planet.title()} would be: {weight_on_planet} kg")
    else:
        print("Invalid planet selection!")


        
if __name__ == "__main__":
    main()
