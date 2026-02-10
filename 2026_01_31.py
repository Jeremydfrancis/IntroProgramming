"""
Jeremy Francis
2026_01_31
Assignment - World Population
"""
world_population = 8_273_231_749
sqmi = 27_878_400 #feet
acre = 43_560 #feet

#Locations
texas_sqft = 7.49e12
wv_sqft = 671.8e9
buenos_aires_sqft = 2.2e9

print (f"The current world population is: {world_population}")

user_input = int(input(
"""Enter a number to fit the whole world population into a specific location:
1). Texas
2). West Virginia
3). Buenos Aires
"""))

if user_input == 1:
      area_sqft = texas_sqft
elif user_input == 2:
      area_sqft = wv_sqft
elif user_input == 3:
      area_sqft = buenos_aires_sqft
else:
      print("Please select a valid option")
      exit()

per_person_sqft = area_sqft / world_population
per_person_sqmi = per_person_sqft / sqmi
per_person_acres = per_person_sqft / acre

print(f"""
Space per person:
Square Feet: {per_person_sqft},
Square Miles: {per_person_sqmi},
Acres: {per_person_acres}
""")


