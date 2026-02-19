"""
Jeremy Francis
2026_02_18
Game Zero Dice Rolling Assignment
"""

import random


def roll_dice(times, sides):
    total = 0
    for i in range(times):
        rolls = random.randint(1, sides)
        total += rolls
    return total


def roll_target(times, sides, target):
    total = 0
    for i in range(times):
        rolls = random.randint(1, sides)
        if rolls >= target:
            total += 1
    return total


def main():
    print("\nWELCOME TO GAME 0 - Dice Rolling Simulator")
    while True:
        while True:
            try:
                roll_times = int(
                    input(
                        "\nHow many times would you like to roll the dice (Enter 0 to quit program)? "
                    )
                )
                if roll_times == 0:
                    return
                if roll_times < 0:
                    print(
                        "\n("
                        + str(roll_times)
                        + ") is Invalid: Please select (0) to exit or an integer greater than 0"
                    )
                    continue
                break
            except ValueError:
                print("Invalid Input Please Try Again")
        while True:
            try:
                dice_sides = int(input("\nHow many sides are on the dice? "))
                if dice_sides <= 1:
                    print(
                        "\n("
                        + str(dice_sides)
                        + ") is Invalid: Please select sides greater than 1"
                    )
                else:
                    break
            except ValueError:
                print("Invalid Input Please Try Again")
        while True:
            try:
                dice_target = int(
                    input(
                        "\nEnter a target number for the dice roll (Enter (0) for no target number): "
                    )
                )
                if dice_target < 0:
                    print(
                        "\n("
                        + str(dice_target)
                        + ") is Invalid: Please select (0) or an integer greater than 0"
                    )
                else:
                    break
            except ValueError:
                print("Invalid Input Please Try Again")
        if dice_target == 0:
            print("\nYou rolled a total of " + str(roll_dice(roll_times, dice_sides)))
        else:
            print(
                "\nYou hit your target "
                + str(dice_target)
                + ", "
                + str(roll_target(roll_times, dice_sides, dice_target))
                + " time(s)"
            )


if __name__ == "__main__":
    main()
