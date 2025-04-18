def main():
    print("Welcome to Planetary Weight Calculator")
    print("-------------------------------------")

    planets_gravity = {"mercury" : 37.6, "venus" : 88.9, "mars" : 37.8, "jupiter" : 236.0, "saturn" : 108.1, "uranus" : 81.5, "neptune" : 114.0}
    planet_gravity_on_earth = []

    for i in planets_gravity:
        result = round(planets_gravity[i] / 100, 3)
        planet_gravity_on_earth.append(result)
    print(planet_gravity_on_earth)
        
    user_weight_on_earth = float(input("Enter your weight on Earth (kg): "))
    print('\nSelect a Planet:')

    for index, planet in enumerate(planets_gravity, start=1):
        print(f"{index}: {planet}")
    select_planet = int(input("Select planet from 1 to 7: "))
    selected_planet = select_planet - 1
    print(user_weight_on_earth * planet_gravity_on_earth[selected_planet])

    # MARS_GRAVITY_ON_EARTH = mars / 100
    # # print(round(MARS_GRAVITY_ON_EARTH, 3))
    
    # MARS_WEIGHT = user_weight_on_earth * MARS_GRAVITY_ON_EARTH
    
    # print(f"The equivalent on Mars: {round(MARS_WEIGHT,1)}")

if __name__ == "__main__":
    main()