"""
Jeremy Francis
2026-01-21
Assignment - Basic Printing

"""
import math
import random

# 1. Ask the user to enter an integer.

user_input = int(input("Enter an Integer: "))

# 2. Print the square root of that integer.

sqr_root = math.sqrt(user_input)
print("The square root of the integer you entered is " + str(sqr_root))

# 3. Print the integer multiplied by pi.

mby_pi = math.pi * user_input
print ("The integer you entered multiplied by PI is " + str(mby_pi))

# 4. Print a few newlines

print ("\n"*3)

# 5. Ask the user to enter their job

job_input = input("Please enter your current job: ")

# 6. Print "Your profession is " and then print the job they entered. (on the same line!)

print("Your profession is " + job_input)

# 7. Generate a random number between (1,1000)

random_number = random.randint(1,1000)

# 8. Print "Your lucky number is" and then print the random number just generated. (again, on the same line.)

print("Your lucky number is " + str(random_number))

# 9. Print a few newlines

print ("\n"*3)

# 10. Print your first name, a tab, your last name, another tab, then your major

print("Jeremy\tFrancis\tComputer Science Tech: Software-AAS")