"""
Jeremy Francis
2026_02_10
CSCT 101 - The Great Pyramid Analysis
"""

import math

while True:
    # MENU
    user_input = input(
        """\nPlease enter a number (1-3) to learn about the following options:
(1) Weight of stone moved each day for 20 years to build the Great Pyramid
(2) Perimeter of Great Pyramid divided by its height
(3) The circumference of a circle that encloses the outside of the Great Pyramid and fills inside as well
(4) Exit program
"""
    )
    # LOGIC
    if user_input == "1":
        total_tons = 5.9e6  # tons
        years_in_total = 20
        days_in_year = 365
        total_days = years_in_total * days_in_year
        tons_per_day = total_tons / total_days
        print(
            "\nTo build the Great Pyramid in 20 years, workers had to move",tons_per_day,"tons of stone per day."
        )
    elif user_input == "2":
        side_length = 230.4
        perimeter = side_length * 4
        height = 146.5
        ratio = perimeter / height
        print(
            "\nThe perimeter divided by height of the Great Pyramid is", ratio
        )  # 2π is the significance I believe?
    elif user_input == "3":
        side_length = 230.4
        small_radius = side_length / 2
        small_circumference = 2 * math.pi * small_radius
        big_radius = (side_length * math.sqrt(2)) / 2
        big_circumference = 2 * math.pi * big_radius
        difference = big_circumference - small_circumference
        print(
            "\nThe difference between the two circumferences is", difference
        )  # tried multiplying by 10, 100, etc. but saw no value but when divided It was closer to π
    elif user_input == "4":
        print("\nYou have exited the program\n")
        break
    else:
        print("Please select a valid option.")
    print()
