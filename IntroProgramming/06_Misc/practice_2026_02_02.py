"""
Jeremy Francis
2026_02_02
High Low Game
"""
# x=0
# while True:
#       print(x)
#       x+=3
#       if x%7 == 0:
#             break
import random

hidden_number = random.randint(1,100)
guesses = 0
while True:
      user_guess = int(input("Try to guess the number "))
      guesses += 1
      if user_guess < hidden_number:
            print("Guess too low")
      elif user_guess > hidden_number:
            print("Guess too high")
      else:
            print("You got it!")
            break

print(f"You took {guesses} guesses to guess the number ")

