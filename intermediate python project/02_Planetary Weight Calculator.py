MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    print(f"\n-----------------PLANETERY_WEIGHT_CALCUTATOR -----------------\n")
    print(f"NAMES OF PLANETS :\n1.mercury\n2.venus\n3.mars\n4.jupiter\n5.saturn\n6.uranus\n7.neptune\n")
    try:
        # Prompt the user for their weight on Earth
        earth_weight = float(input("Enter a weight on Earth: "))
        
        # Prompt the user for the name of a planet
        planet = input("Enter a planet : ").lower().strip()
        
        # Determine the gravitational constant using if-elif statements
        if planet == "mercury":
            gravity_constant = MERCURY_GRAVITY
        elif planet == "venus":
            gravity_constant = VENUS_GRAVITY
        elif planet == "mars":
            gravity_constant = MARS_GRAVITY
        elif planet == "jupiter":
            gravity_constant = JUPITER_GRAVITY
        elif planet == "saturn":
            gravity_constant = SATURN_GRAVITY
        elif planet == "uranus":
            gravity_constant = URANUS_GRAVITY
        elif planet == "neptune":
            gravity_constant = NEPTUNE_GRAVITY
        else:
            print("Invalid planet name. Please enter one of the planets in our solar system.")
            return
        
        # Calculate the equivalent weight on the selected planet
        planetary_weight = earth_weight * gravity_constant
        rounded_planetary_weight = round(planetary_weight, 2)
        
        # Print the result
        print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight))
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for weight.")


main()
