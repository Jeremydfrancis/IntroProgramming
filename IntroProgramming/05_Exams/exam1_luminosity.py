"""
Jeremy Francis
2026_03_04
Exam 1
"""

import math


# luminosity formula
def calc_luminosity(radius, temp):
    stef_constant = 5.67e-8  # stefan boltzmann constant
    luminosity = 4 * math.pi * (radius**2) * stef_constant * (temp**4)
    return luminosity


def get_radius():
    while True:
        # TRY AND EXCEPT BLOCK TO HANDLE ERRORS
        try:
            user_radius = float(input("Please enter the stars radius (0 to quit): "))
            if user_radius < 0:
                print("please enter a number greater than 0")
            else:
                break
        except ValueError:
            print("Invalid entry: please enter a number greater than 0")
    return user_radius


def get_temp():
    while True:
        # TRY AND EXCEPT BLOCK TO HANDLE ERRORS
        try:
            user_temp = float(input("Please enter the stars temperature (0 to quit): "))
            if user_temp < 0:
                print("please enter a number greater than 0")
            else:
                break
        except ValueError:
            print("Invalid entry: please enter a number greater than 0")
    return user_temp


def main():
    # CONSTANTS
    dwarf = 3.828e27
    giant = 3.828e29
    # CLASSES
    dwarf_count = 0
    giant_count = 0
    super_giant_count = 0
    # RUNNING TOTALS
    total_stars = 0
    count = 0
    min_lum = None
    max_lum = None
    while True:
        user_radius = get_radius()
        # QUIT PROGRAM IF USER ENTERS 0
        if user_radius == 0:
            break
        user_temp = get_temp()
        if user_temp == 0:
            break
        luminosity = calc_luminosity(user_radius, user_temp)
        print(f"\nThe luminosity is: {luminosity}")
        # ADD +1 COUNT FOR EACH ITERATION
        count += 1
        total_stars += luminosity
        # MAINTAIN MIN VALUE
        if min_lum is None or luminosity < min_lum:
            min_lum = luminosity
        # MAINTAIN MAX VALUE
        if max_lum is None or luminosity > max_lum:
            max_lum = luminosity
        # TOTALS FOR CLASSES
        if luminosity < dwarf:
            dwarf_count += 1
        elif luminosity < giant:
            giant_count += 1
        else:
            super_giant_count += 1
        print(
            f"""
TOTAL STARS: {count}
AVERAGE LUMINOSITY: {total_stars/count} watts
MINIMUM LUMINOSITY: {min_lum} watts
MAXIMUM LUMINOSITY: {max_lum} watts
TOTAL DWARF STARS: {dwarf_count}
TOTAL GIANT STARS: {giant_count}
TOTAL SUPERGIANT STARS: {super_giant_count}

"""
        )


if __name__ == "__main__":
    main()
