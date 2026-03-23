"""
Jeremy Francis
2026_02_24
World Population Refactored
"""

world_population = 8_273_231_749
sqmi = 27_878_400  # feet
acre = 43_560  # feet

# Locations
texas_sqft = 7.49e12
wv_sqft = 671.8e9
buenos_aires_sqft = 2.2e9


def select_location(area):
    if area == 1:
        space_per_person("Texas", texas_sqft)
    elif area == 2:
        space_per_person("West Virginia", wv_sqft)
    elif area == 3:
        space_per_person("Buenos Aires", buenos_aires_sqft)
    else:
        print("Please select a valid option")
        exit()


def space_per_person(location_name, area_sqft):
    per_person_sqft = area_sqft / world_population
    per_person_sqmi = per_person_sqft / sqmi
    per_person_acres = per_person_sqft / acre
    print(
        f"""
Space per person in {location_name}:
Square Feet: {per_person_sqft},
Square Miles: {per_person_sqmi},
Acres: {per_person_acres}
"""
    )


def get_input():
    while True:
        try:
            user_input = int(
                input(
                    """Enter a number to fit the whole world population into a specific location:
1). Texas
2). West Virginia
3). Buenos Aires
"""
                )
            )
            if user_input < 1 or user_input > 3:
                print("Please select a valid number from the menu")
            else:
                break

        except ValueError:
            print("Please select a number from the menu")
    return user_input


def main():
    print(f"The current world population is: {world_population}")
    user_input = get_input()
    select_location(user_input)


if __name__ == "__main__":
    main()
