"""
Jeremy Francis
2026_02_18
my_utilities.py
"""
import random
# user_input = int(input("how many iterations? "))
# for i in range(1,user_input + 1):
#       print(i)
def roll_dice(times,sides):
      total = 0 #accumulator variable
      for i in range(times):
            roll = random.randint(1,sides)
            total += roll
      return total
def roll_target(times,sides,target):
      total = 0 #accumulator variable
      for i in range(times):
            roll = random.randint(1,sides)
            if roll == target:
      return total
# while True:
#       print("Strength: " + str(roll_dice(3,6)))
#       print("Dexterity: " + str(roll_dice(3,6)))
#       print("Constitution: " + str(roll_dice(3,6)))
#       print("Wisdom: " + str(roll_dice(3,6)))
#       print("Intelligence: " + str(roll_dice(3,6)))
#       print("Charisma: " + str(roll_dice(3,6)))
#       user_input = input("Generate another (Y/N)\n").upper()
#       if user_input =="N":
#             break

def main():
      print("Program Started.")
      print(roll_dice(1,20))

if __name__ == "__main__":
      main()





