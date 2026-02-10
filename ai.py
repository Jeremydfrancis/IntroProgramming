# World Population "Fit Everyone in Texas" Calculator
# Requirements met:
# - Prints current world population
# - Offers 3+ location choices (includes Texas)
# - Stores each location's area starting in SQUARE FEET
# - Converts square feet -> square miles and acres in Python
# - Computes AREA PER PERSON (not people per area)

WORLD_POPULATION = 8_271_596_070  # as of 2026-01-29 (Worldometer / UN estimates)

SQFT_PER_SQMI = 27_878_400
SQFT_PER_ACRE = 43_560


def sqft_to_sqmi(area_sqft: float) -> float:
    return area_sqft / SQFT_PER_SQMI


def sqft_to_acres(area_sqft: float) -> float:
    return area_sqft / SQFT_PER_ACRE


def print_results(location_name: str, area_sqft: float) -> None:
    area_per_person_sqft = area_sqft / WORLD_POPULATION
    area_per_person_sqmi = sqft_to_sqmi(area_per_person_sqft)
    area_per_person_acres = sqft_to_acres(area_per_person_sqft)

    print("\n" + "=" * 60)
    print(f"Location: {location_name}")
    print(f"World population used: {WORLD_POPULATION:,}")
    print("-" * 60)
    print("AREA PER PERSON")
    print(f"  Square Feet : {area_per_person_sqft:,.6f} sq ft/person")
    print(f"  Square Miles: {area_per_person_sqmi:,.12f} sq mi/person")
    print(f"  Acres       : {area_per_person_acres:,.12f} acres/person")
    print("=" * 60 + "\n")


def main() -> None:
    # Base areas: START IN SQUARE FEET (then convert from that)
    # Notes: These were computed from published areas:
    # Texas land area: 261,232 sq mi
    # West Virginia land area: 24,078 sq mi
    # Buenos Aires (city) area: 78 sq mi
    locations = {
        "1": ("Texas (land area)", 261_232 * SQFT_PER_SQMI),
        "2": ("West Virginia (land area)", 24_078 * SQFT_PER_SQMI),
        "3": ("Buenos Aires, Argentina (city proper)", 78 * SQFT_PER_SQMI),
    }

    print(f"Current world population: {WORLD_POPULATION:,}\n")

    print("Choose a location to fit the whole world population into:\n")
    for key, (name, _) in locations.items():
        print(f"  {key}) {name}")

    choice = input("\nEnter 1, 2, or 3: ").strip()

    if choice not in locations:
        print("\nInvalid choice. Please run again and pick 1, 2, or 3.\n")
        return

    location_name, area_sqft = locations[choice]
    print_results(location_name, area_sqft)


if __name__ == "__main__":
    main()
