"""
Jeremy Francis
2026_01_21
Weight calculation module for the application.

"""

# Create a program which ask the user for their current weight and ask them 
# for their target weight. Then tell the user how much they would need to 
# lose per day if they wanted to lose it in 30 days.

while True:   
    try:
        #figure out current weight
        user_input = input("Enter your current weight in pounds: ")
        weight = float(user_input)
        print("Your current weight is:", str(weight), "pounds")
        #figure out target weight
        target_input = input("Enter your target weight in pounds:")
        target_weight = float(target_input)
        print("Your target weight is:", str(target_weight), "pounds")
        #calculate weight loss per day
        weight_loss = weight - target_weight
        daily_loss = weight_loss / 30
        print("To reach your target weight in 30 days, you need to lose", 
              str(daily_loss), "pounds per day.")
        break
    except ValueError:
        print("Please enter a valid number for your weight.")


