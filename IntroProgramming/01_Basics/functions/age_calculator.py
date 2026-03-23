"""
Jeremy Francis
2026_01_14
Index module for the application.

"""

# print('He said, "Hello, I\'m World!"')
while True:
    try:
        user_input = input("Enter your age: ")
        new_age = int(user_input) + 2
        print("In two years, you will be:", str(new_age))
        print("Welcome to the application!")
    except ValueError:
        print("Please enter a valid number for your age.")

